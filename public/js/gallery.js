/* links-digest gallery.js — Dynamic MD parsing + rendering */

// ── State ────────────────────────────────────────────────────────────────────

let cards = [];
let filtered = [];
let sortMode = 'date';
let groupMode = 'section';
let viewMode = 'card';
let cardMinWidth = 360;
let jsZipLoaded = false;

const STORE_KEY = 'links-digest-gallery';

// ── Gray-matter parsing (lightweight, no deps) ───────────────────────────────

function parseFrontmatter(text) {
  // Match YAML frontmatter between --- delimiters
  const match = text.match(/^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/);
  if (!match) return { data: {}, content: text };

  const [_, yaml, content] = match;
  const data = {};

  // Simple YAML parser for flat key: value + arrays
  for (const line of yaml.split('\n')) {
    const arrMatch = line.match(/^(\w+):\s*\[(.+)\]$/);
    const strMatch = line.match(/^(\w+):\s*"(.+)"$/);
    const plainMatch = line.match(/^(\w+):\s*(.+)$/);

    if (arrMatch) {
      data[arrMatch[1]] = arrMatch[2].split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
    } else if (strMatch) {
      data[strMatch[1]] = strMatch[2];
    } else if (plainMatch) {
      let val = plainMatch[2];
      if (val === 'null') val = null;
      else if (val === 'true') val = true;
      else if (val === 'false') val = false;
      data[plainMatch[1]] = val;
    }
  }

  return { data, content };
}

// ── Section detection from tags ──────────────────────────────────────────────

const SECTION_MAP = {
  knowledge: ['knowledge', 'second-brain', 'RAG', 'wiki', 'graph'],
  agents: ['agent', 'MCP', 'browser', 'automation'],
  devtools: ['CLI', 'developer-tools', 'token', 'fuzzy-search'],
  voice: ['TTS', 'voice', 'audio'],
  llm: ['LLM', 'transformer', 'model', 'GPT', 'Qwen', 'Llama'],
};

function detectSection(tags) {
  const tagLower = (tags || []).map(t => t.toLowerCase());
  for (const [section, keywords] of Object.entries(SECTION_MAP)) {
    if (keywords.some(k => tagLower.includes(k.toLowerCase()))) {
      return section;
    }
  }
  return 'other';
}

// ── Load MD files ────────────────────────────────────────────────────────────

async function loadLinks() {
  // Fetch the directory listing via a manifest or API
  // For static hosting, we use a pre-generated manifest.json
  let files = [];

  try {
    const manifestRes = await fetch('links/manifest.json');
    if (manifestRes.ok) {
      files = await manifestRes.json();
    }
  } catch {
    // Fallback: try to parse directory listing (won't work on CF Pages)
    console.warn('No manifest.json found, gallery may be empty');
  }

  // Fetch and parse each MD file
  cards = [];
  for (const file of files) {
    try {
      const res = await fetch(`links/${file}`);
      if (!res.ok) continue;
      const text = await res.text();
      const { data, content } = parseFrontmatter(text);

      cards.push({
        file,
        title: data.title || file,
        source: data.source || '#',
        date: data.date || '2026-01-01',
        tags: data.tags || [],
        platform: data.platform || 'web',
        author: data.author,
        summary: data.summary || '',
        content,
        section: detectSection(data.tags),
      });
    } catch (e) {
      console.error(`Failed to load ${file}:`, e);
    }
  }

  // Sort by date descending by default
  cards.sort((a, b) => b.date.localeCompare(a.date));
  filtered = [...cards];
}

// ── Filters ──────────────────────────────────────────────────────────────────

const filters = {};

const FILTER_DIMS = {
  section: {
    label: 'Section',
    fn: c => c.section,
  },
  platform: {
    label: 'Platform',
    fn: c => c.platform,
  },
};

function applyFilters() {
  let result = [...cards];

  // Apply active filters
  for (const [dim, val] of Object.entries(filters)) {
    if (val && val !== 'all') {
      result = result.filter(c => FILTER_DIMS[dim].fn(c) === val);
    }
  }

  // Search
  const q = (document.getElementById('searchInput').value || '').toLowerCase();
  if (q) {
    result = result.filter(c => {
      const hay = [c.title, c.summary, ...c.tags, c.source, c.author || ''].join(' ').toLowerCase();
      return hay.includes(q);
    });
  }

  filtered = result;
}

// ── Sorting ──────────────────────────────────────────────────────────────────

function sortCards(arr) {
  if (sortMode === 'title') return [...arr].sort((a, b) => a.title.localeCompare(b.title));
  if (sortMode === 'platform') return [...arr].sort((a, b) => a.platform.localeCompare(b.platform));
  return [...arr].sort((a, b) => b.date.localeCompare(a.date));
}

// ── Grouping ──────────────────────────────────────────────────────────────────

const GROUP_TITLES = {
  knowledge: '📚 Knowledge',
  agents: '🤖 AI Agents',
  devtools: '🔧 Developer Tools',
  voice: '🎙️ Voice & TTS',
  llm: '🧠 LLM & Models',
  other: '📎 Other',
};

function groupCards(arr, dim) {
  const groups = {};
  for (const c of arr) {
    const key = dim === 'section' ? c.section : c[dim];
    if (!groups[key]) groups[key] = [];
    groups[key].push(c);
  }
  return groups;
}

// ── Rendering ────────────────────────────────────────────────────────────────

function escHtml(str) {
  if (!str) return '';
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function mkBadge(platform) {
  const labels = { github: 'GitHub', x: 'X', web: 'Web', reddit: 'Reddit', gist: 'Gist', youtube: 'YouTube' };
  return `<span class="bdg bdg-${platform}">${labels[platform] || platform}</span>`;
}

function mkCard(c) {
  const tags = (c.tags || []).slice(0, 3).map(t => `<span class="tag">${escHtml(t)}</span>`).join('');
  return `<div class="link-card" data-file="${escHtml(c.file)}" data-title="${escHtml(c.title)}">
    <div class="card-hdr">
      <div class="card-date">${escHtml(c.date)}</div>
      <div class="card-title">${escHtml(c.title)}</div>
    </div>
    <div class="card-body">
      <div class="badges">${mkBadge(c.platform)}</div>
      <div class="card-summary">${escHtml(c.summary)}</div>
      <div class="card-source">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
        <a href="${escHtml(c.source)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">${escHtml(c.source)}</a>
      </div>
      ${tags ? '<div class="tags">' + tags + '</div>' : ''}
      <div class="card-actions">
        <button class="dl-btn" onclick="event.stopPropagation(); downloadFile('${escHtml(c.file)}')">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
          Download
        </button>
        <span class="expand-hint">Click to expand →</span>
      </div>
    </div>
  </div>`;
}

function render() {
  const el = document.getElementById('gallery');
  applyFilters();
  const sorted = sortCards(filtered);
  const total = cards.length;

  if (!sorted.length) {
    el.innerHTML = '<div class="empty">No links match the current filters.</div>';
    document.getElementById('stats').textContent = `0 / ${total}`;
    return;
  }

  // List view
  if (viewMode === 'list') {
    el.innerHTML = renderListView(sorted);
    document.getElementById('stats').textContent = `${sorted.length} / ${total}`;
    return;
  }

  // Card view with optional grouping
  if (groupMode === 'none') {
    el.innerHTML = `<div class="card-grid" style="grid-template-columns:repeat(auto-fill,minmax(${cardMinWidth}px,1fr))">${sorted.map(mkCard).join('')}</div>`;
  } else {
    const groups = groupCards(sorted, groupMode);
    const order = ['knowledge', 'agents', 'devtools', 'voice', 'llm', 'other'];
    let html = '';
    for (const key of order) {
      const gCards = groups[key];
      if (!gCards?.length) continue;
      const title = GROUP_TITLES[key] || key.toUpperCase();
      html += `<div class="group-hdr">
        <span class="group-tag">${escHtml(title)}</span>
        <span class="group-cnt">${gCards.length}</span>
      </div>
      <div class="card-grid" style="grid-template-columns:repeat(auto-fill,minmax(${cardMinWidth}px,1fr))">
        ${gCards.map(mkCard).join('')}
      </div>`;
    }
    el.innerHTML = html;
  }

  document.getElementById('stats').textContent = `${sorted.length} / ${total}`;
}

function renderListView(arr) {
  const rows = arr.map(c => `<div class="list-row" data-file="${escHtml(c.file)}" data-title="${escHtml(c.title)}">
    <span class="list-date">${escHtml(c.date)}</span>
    <span class="list-title">${escHtml(c.title)}</span>
    <span class="list-source">${escHtml(c.platform)}</span>
    <span class="list-tags">${(c.tags || []).slice(0, 2).map(t => `<span class="tag">${escHtml(t)}</span>`).join('')}</span>
  </div>`).join('');
  return `<div class="list-view">${rows}</div>`;
}

// ── Size control ─────────────────────────────────────────────────────────────

function resizeCards(d) {
  cardMinWidth = Math.max(280, Math.min(600, cardMinWidth + d));
  document.getElementById('sizeLabel').textContent = cardMinWidth;
  document.querySelectorAll('.card-grid').forEach(g => {
    g.style.gridTemplateColumns = `repeat(auto-fill,minmax(${cardMinWidth}px,1fr))`;
  });
}

// ── Downloads ────────────────────────────────────────────────────────────────

async function downloadFile(filename) {
  try {
    const r = await fetch(`links/${filename}`);
    if (!r.ok) throw new Error(r.status);
    const blob = await r.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  } catch (e) {
    showToast('Download failed: ' + e.message, true);
  }
}

async function loadJSZip() {
  if (jsZipLoaded || window.JSZip) {
    jsZipLoaded = true;
    return true;
  }
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js';
    script.onload = () => { jsZipLoaded = true; resolve(true); };
    script.onerror = () => reject(new Error('JSZip blocked by CSP'));
    document.head.appendChild(script);
  });
}

async function downloadAllAsZip() {
  const btn = document.getElementById('dlAllMd');
  btn.dataset.loading = 'true';

  try {
    await loadJSZip();
    const zip = new JSZip();

    for (const c of cards) {
      const r = await fetch(`links/${c.file}`);
      if (r.ok) {
        const text = await r.text();
        zip.file(c.file, text);
      }
    }

    const blob = await zip.generateAsync({ type: 'blob' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'links-digest.zip';
    a.click();
    URL.revokeObjectURL(url);
    showToast(`Downloaded links-digest.zip with ${cards.length} files`);
  } catch (e) {
    showToast('Download failed: ' + e.message, true);
  } finally {
    btn.dataset.loading = 'false';
  }
}

// ── Toast ────────────────────────────────────────────────────────────────────

function showToast(msg, isErr = false) {
  const el = document.createElement('div');
  el.className = 'toast' + (isErr ? ' err' : '');
  el.textContent = msg;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 3000);
}

// ── Modal ────────────────────────────────────────────────────────────────────

async function openContentModal(cardEl) {
  const file = cardEl.dataset.file;
  const title = cardEl.dataset.title;
  const card = cards.find(c => c.file === file);

  const modal = document.getElementById('contentModal');
  const body = document.getElementById('modalBody');

  document.getElementById('modalTitle').textContent = title;
  document.getElementById('modalDate').textContent = card?.date || '';
  document.getElementById('modalSource').href = card?.source || '#';
  document.getElementById('modalDl').href = `links/${file}`;

  body.className = 'modal-body loading';
  body.innerHTML = '';
  modal.classList.add('active');

  try {
    const r = await fetch(`links/${file}`);
    if (!r.ok) throw new Error(r.status);
    const md = await r.text();
    body.className = 'modal-body';
    body.innerHTML = '<div class="md-content">' + renderMarkdown(md) + '</div>';
  } catch (e) {
    body.className = 'modal-body';
    body.innerHTML = '<div style="color:var(--red)">Failed to load content: ' + escHtml(e.message) + '</div>';
  }
}

function closeContentModal() {
  document.getElementById('contentModal').classList.remove('active');
}

function closeContentModalOutside(e) {
  if (e.target === document.getElementById('contentModal')) closeContentModal();
}

// ── Simple Markdown renderer ─────────────────────────────────────────────────

function renderMarkdown(md) {
  let html = md
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/^### (.*$)/gm, '<h2>$1</h2>')
    .replace(/^## (.*$)/gm, '<h2>$1</h2>')
    .replace(/^# (.*$)/gm, '<h1>$1</h1>')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/```(\w*)\n([\s\S]*?)```/g, '<pre><code>$2</code></pre>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
    .replace(/^---$/gm, '<hr>')
    .replace(/^- (.*$)/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>')
    .replace(/^\|(.+)\|$/gm, (m, row) => {
      const cells = row.split('|').map(c => c.trim());
      if (cells.every(c => c.match(/^-+$/))) return '<!-- skip -->';
      return '<tr>' + cells.map(c => `<td>${c}</td>`).join('') + '</tr>';
    })
    .replace(/(<tr>.*<\/tr>\n?)+/g, '<table>$&</table>')
    .replace(/<!-- skip -->\n/g, '')
    .replace(/\n\n/g, '</p><p>')
    .replace(/^(?!<[hpultbhcod])/gm, '<p>')
    .replace(/(?<![>])$/gm, '</p>')
    .replace(/<p><\/p>/g, '')
    .replace(/<p>(<[hupltb])/g, '$1')
    .replace(/(<\/[hupltb].*>)<\/p>/g, '$1');

  return html;
}

// ── Theme ────────────────────────────────────────────────────────────────────

function initTheme() {
  const stored = localStorage.getItem(STORE_KEY + '-theme') || 'dark';
  document.documentElement.dataset.theme = stored;
}

function toggleTheme() {
  const current = document.documentElement.dataset.theme;
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = next;
  localStorage.setItem(STORE_KEY + '-theme', next);
}

// ── Wire controls ─────────────────────────────────────────────────────────────

function wireSegs(containerId, callback) {
  document.querySelectorAll(`#${containerId} .seg`).forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll(`#${containerId} .seg`).forEach(b => b.classList.remove('on'));
      btn.classList.add('on');
      callback(btn.dataset.v);
    });
  });
}

function buildFilterButtons() {
  const dims = ['section', 'platform'];
  const bar = document.getElementById('filterBar');

  for (const dim of dims) {
    const values = [...new Set(cards.map(c => c[dim]))].sort();

    // Create container
    const ctrl = document.createElement('div');
    ctrl.className = 'ctrl';
    ctrl.innerHTML = `<span class="ctrl-label">${FILTER_DIMS[dim].label}</span><div class="segs" id="${dim}Filter"><button class="seg on" data-v="all">All</button></div>`;
    bar.appendChild(ctrl);

    // Add buttons
    const segs = ctrl.querySelector('.segs');
    for (const val of values) {
      const btn = document.createElement('button');
      btn.className = 'seg';
      btn.dataset.v = val;
      btn.textContent = val.charAt(0).toUpperCase() + val.slice(1);
      segs.appendChild(btn);
    }

    // Wire
    wireSegs(`${dim}Filter`, v => {
      filters[dim] = v === 'all' ? null : v;
      render();
    });
  }
}

// ── Init ─────────────────────────────────────────────────────────────────────

async function init() {
  initTheme();
  await loadLinks();
  buildFilterButtons();
  render();

  // Wire controls
  wireSegs('sortSegs', v => { sortMode = v; render(); });
  wireSegs('viewSegs', v => {
    viewMode = v;
    const sizeCtrl = document.querySelector('.size-btn')?.closest('.ctrl');
    if (sizeCtrl) sizeCtrl.style.display = viewMode === 'list' ? 'none' : 'flex';
    render();
  });
  wireSegs('groupSegs', v => { groupMode = v; render(); });

  // Search
  document.getElementById('searchInput').addEventListener('input', render);

  // Theme
  document.getElementById('themeBtn').addEventListener('click', toggleTheme);

  // Download dropdown
  document.getElementById('dlToggle').addEventListener('click', () => {
    document.getElementById('dlMenu').classList.toggle('open');
  });
  document.addEventListener('click', e => {
    const wrap = document.getElementById('dlWrap');
    if (!wrap.contains(e.target)) {
      document.getElementById('dlMenu').classList.remove('open');
    }
  });
  document.getElementById('dlAllMd').addEventListener('click', async () => {
    document.getElementById('dlMenu').classList.remove('open');
    await downloadAllAsZip();
  });

  // Modal
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeContentModal();
  });

  // Card click delegation
  document.getElementById('gallery').addEventListener('click', e => {
    const card = e.target.closest('.link-card, .list-row');
    if (card && !e.target.closest('a, button')) {
      openContentModal(card);
    }
  });

  // Update header count
  document.querySelector('.header-left .sub').textContent = `Channel #links · RoxabiFactory · ${cards.length} liens`;
}

document.addEventListener('DOMContentLoaded', init);

// ── Live reload via SSE (dev only) ─────────────────────────────────────────────
if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {
  (function() {
    let es;
    function connect() {
      es = new EventSource('/api/events');
      es.onmessage = function(e) {
        try {
          const msg = JSON.parse(e.data);
          if (msg.type === 'reload') {
            console.log('[live-reload] manifest changed:', msg.changed);
            loadLinks().then(render);
          }
        } catch(_) {}
      };
      es.onerror = function() { es.close(); setTimeout(connect, 5000); };
    }
    connect();
  })();
}
