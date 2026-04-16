# Changelog

## 0.1.0 (2026-04-16)


### Features

* add LLM enrichment for scraped links ([59ed912](https://github.com/Roxabi/roxabi-intel/commit/59ed9123d7e592fb04429ae833de2e8c008b2319))
* add summary to frontmatter for card display ([2e47e3d](https://github.com/Roxabi/roxabi-intel/commit/2e47e3ddce9f1787bf54c55ff0828517ed9bf67f))
* **gallery:** add Open Graph and Twitter Card meta tags ([5bedc67](https://github.com/Roxabi/roxabi-intel/commit/5bedc6798f4ebecd96f17b0ade20e8c8dbaf683f))
* **gallery:** lazy-load via baked index.json + untrack public/links ([b7e777a](https://github.com/Roxabi/roxabi-intel/commit/b7e777a7aefe81b8c6ce93685ff0e217d66d36a2))
* **gallery:** show summary in list view, dark-grey, takes remaining space ([e816525](https://github.com/Roxabi/roxabi-intel/commit/e816525ec211c6be1f4a0b452980c0327d5bd12a))
* **intel:** render key_points + reply + collapsible source in modal ([fa09e04](https://github.com/Roxabi/roxabi-intel/commit/fa09e044f1f092ec2f9254494395537137995bc5))
* **links:** add 180+ new link entries from March-April 2026 ([5bfa859](https://github.com/Roxabi/roxabi-intel/commit/5bfa85943a1b836147c2e1ac35fb1a75a9080b0c))
* **links:** import 425 vault links + migrate storage to ~/roxabi/links ([1f0b590](https://github.com/Roxabi/roxabi-intel/commit/1f0b5906c661a7afa08c3f27a0b8bb2145c21d3a))
* read Discord token from Lyra CredentialStore ([38dcfaa](https://github.com/Roxabi/roxabi-intel/commit/38dcfaa022f5f6f8489f955045db3305846fa3be))
* **supervisor:** register with hub + add program config ([1a97101](https://github.com/Roxabi/roxabi-intel/commit/1a971019bb443cd39be8e916c2796fcbc8f5f301))


### Bug Fixes

* add CF account ID to deploy + fix lint errors ([680c030](https://github.com/Roxabi/roxabi-intel/commit/680c0302ade42ae13bc7a3d302c7773c2ad714e9))
* **build:** copy MDs and index to public/links/ matching gallery.js fetch paths ([be8d130](https://github.com/Roxabi/roxabi-intel/commit/be8d130b3d2fff45d98792ba15d9c663a91db662))
* **ci:** add both links-digest and roxabi-intel to license allowlist ([22b0cf5](https://github.com/Roxabi/roxabi-intel/commit/22b0cf5085d3de8d0aa9597cbaa7591182695800))
* **ci:** add roxabi-intel to license allowlist after rename ([c14286c](https://github.com/Roxabi/roxabi-intel/commit/c14286cbced27b6279e1e0d02b8b62a1080d4f8c))
* clean summary output and improve markdown rendering ([d9af508](https://github.com/Roxabi/roxabi-intel/commit/d9af5082a8ae05d201a3dbb8e5a494a11da2767c))
* **config:** correct INTEL_DIR path to ~/.roxabi/intel ([356f656](https://github.com/Roxabi/roxabi-intel/commit/356f656e3bcce3e59436c0311db4c673f7248861))
* **deploy:** load Cloudflare credentials from .env ([c58224a](https://github.com/Roxabi/roxabi-intel/commit/c58224adc0ad614f3b60c3d428c62d1fcdc288b4))
* **digest:** extract clean content for X tweets and Gists ([e142939](https://github.com/Roxabi/roxabi-intel/commit/e1429399aff1fdcaa06a942c2c2e24f799b74f6b))
* **digest:** point at live roxabi-plugins source + strip query from github slug ([4025e5f](https://github.com/Roxabi/roxabi-intel/commit/4025e5f6662b62695b96944a06a550016b9307c5))
* **digest:** prefer marketplace web-intel cache over live source ([226191e](https://github.com/Roxabi/roxabi-intel/commit/226191ea6b8a79aaa9e2ab571dd1e5e0e983fce1))
* **digest:** validate enrichment output + re-enrich 41 stale files ([95f1a0b](https://github.com/Roxabi/roxabi-intel/commit/95f1a0b659cb30c4169f4a7e21d88c901997adfc))
* **gallery:** decode \uXXXX escapes in frontmatter + remove dead t.co placeholder ([7e28c55](https://github.com/Roxabi/roxabi-intel/commit/7e28c556ad7255fc224e5705eb5eae4899ebebf2))
* **gallery:** default group = date (was section) ([a10ca97](https://github.com/Roxabi/roxabi-intel/commit/a10ca97642ddbfe8d7a9f4365648fe420de61090))
* **gallery:** grouping by date/platform + persist settings in localStorage ([647d95d](https://github.com/Roxabi/roxabi-intel/commit/647d95db1ca0a299d2ffb980d2f90edd53ad2959))
* **gallery:** list-view summary flows right after title in single flex cell ([20776e6](https://github.com/Roxabi/roxabi-intel/commit/20776e64138155712f34f3f5c55dc624d28c0fff))
* **gallery:** preserve whitespace inside fenced code blocks in modal ([6b8d73e](https://github.com/Roxabi/roxabi-intel/commit/6b8d73e3faa51b277c264c44e9ef02f309a3c69b))
* **gallery:** stack title above summary in list view, never truncate title ([115050d](https://github.com/Roxabi/roxabi-intel/commit/115050d03978e7d4bb0bd121983734644b07ede3))
* **gallery:** use marked + DOMPurify for modal markdown render ([8046467](https://github.com/Roxabi/roxabi-intel/commit/80464671ee51e1641d9dac5fe8e0045552fdb047))
* handle empty arrays in YAML parser and rename ? files ([8e5fb34](https://github.com/Roxabi/roxabi-intel/commit/8e5fb34c0dc31308bc11a1490d8ca030d6495316))
* **intel:** correct INTEL_DIR path from ~/roxabi to ~/.roxabi ([0679895](https://github.com/Roxabi/roxabi-intel/commit/06798955a50ecfe7ef60fefecc7ed4d56a0f9fa9))
* **intel:** run digest before deploy to fetch latest links ([d552e78](https://github.com/Roxabi/roxabi-intel/commit/d552e7822d0417ef4ebd6eb2294c8e728e0e8db7))
* **intel:** skip URLs with existing MD files to avoid re-scraping ([2d38cc8](https://github.com/Roxabi/roxabi-intel/commit/2d38cc877e845a4820c694db2f1db84bde078e3a))
* **license:** add links-digest to allowlist ([c6b4d81](https://github.com/Roxabi/roxabi-intel/commit/c6b4d8171c240414b47e6737343200d6e2b88ab4))
* **links:** re-enrich stragglers now that digest points at live web-intel ([342aa12](https://github.com/Roxabi/roxabi-intel/commit/342aa1289a6413505778db1d3054cd3cbc4ae366))
* **serve:** emit simple-list manifest compatible with gallery.js ([7e776ce](https://github.com/Roxabi/roxabi-intel/commit/7e776ce17f45647454b225a611a3556b72b08394))
* **template:** dedupe title/summary when scraper content is present ([7a6ec0c](https://github.com/Roxabi/roxabi-intel/commit/7a6ec0cc3222c3e9d34aa279fa02e95ccf2a3196))
* use DISCORD_TOKEN env var instead of CredentialStore ([50b6aef](https://github.com/Roxabi/roxabi-intel/commit/50b6aefc7884472c3c028b7a05500747214bf933))


### Documentation

* drop commit/push asking rule, keep destructive-ops guard ([5a59dec](https://github.com/Roxabi/roxabi-intel/commit/5a59decc369239aa26ab531721b9644694be051e))
