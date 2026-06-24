## 블로그 작성 원칙

- 모든 블로그 콘텐츠는 **한국어**로 작성한다.
- 폰트는 별도의 라이선스 없이 누구나 사용 가능한 **보편적인 웹 폰트**를 사용한다. SF Pro는 Apple 전용이므로 시스템 폰트 스택으로 대체한다:
  - **본문 / UI:** `system-ui, -apple-system, "Noto Sans KR", sans-serif` — 한글은 Noto Sans KR로 보완
  - **코드 블록:** `"JetBrains Mono", "Source Code Pro", monospace`
  - serif 계열은 사용하지 않는다. Apple 디자인은 단일 sans-serif 시스템이다.

---

## Overview

Apple's web presence is a masterclass in **reverent product photography framed by near-invisible UI**. Every page is a stack of edge-to-edge product "tiles" — alternating light and dark canvases, each centered on a hero headline, a one-line tagline, two tiny blue pill CTAs, and an impossibly crisp product render. Nothing competes with the product. Typography is confident but quiet; color is either pure white, an off-white parchment, or a near-black tile; interactive elements are a single, quiet blue.

Density is unusually low even by contemporary SaaS standards. Each tile occupies roughly one viewport, and there is no decorative chrome — no borders, no gradients, no decorative frames, no shadows on headlines. Elevation appears only when a product image rests on a surface (a single soft `rgba(0, 0, 0, 0.22) 3px 5px 30px` drop for visual weight). The result is a catalog that feels more like a museum gallery: the wall disappears and the artifact takes over.

**Key Characteristics:**
- Photography-first presentation; UI recedes so the product can speak.
- Alternating full-bleed tile sections: white/parchment ↔ near-black, with the color change itself acting as the section divider.
- Single blue accent (`{colors.primary}` — #0066cc) carries every interactive element. No second brand color exists.
- Two button grammars: tiny blue pill CTAs (`{rounded.pill}`) and compact utility rects (`{rounded.sm}`).
- SF Pro Display + SF Pro Text — negative letter-spacing at display sizes for the signature "Apple tight" headline feel.
- Whisper-soft elevation used only when a product image needs to breathe — exactly one drop-shadow in the entire system.
- Tight two-row nav: slim `{component.global-nav}` + product-specific `{component.sub-nav-frosted}` with persistent right-aligned primary CTA.

## Colors

### Brand & Accent
- **Action Blue** (`{colors.primary}` — #0066cc): The single brand-level interactive color. All text links, all blue pill CTAs, and the focus ring root.
- **Sky Link Blue** (`{colors.primary-on-dark}` — #2997ff): A brighter blue used on dark surfaces for in-copy links and inline callouts.

### Surface
- **Pure White** (`{colors.canvas}` — #ffffff): The dominant canvas.
- **Parchment** (`{colors.canvas-parchment}` — #f5f5f7): The signature Apple off-white. Used for alternating light tiles and footer.
- **Near-Black Tile** (`{colors.surface-dark}` — #1d1d1f): Primary dark surface.
- **Pure Black** (`{colors.surface-black}` — #000000): Reserved for nav bar background.

### Text
- **Near-Black Ink** (`{colors.ink}` — #1d1d1f): All headlines and body text on light surfaces.
- **Body On Dark** (`{colors.on-dark}` — #ffffff): All text on dark tiles.
- **Body Muted** (`{colors.muted}` — #6e6e73): Secondary copy on light surfaces.
- **Body Muted On Dark** (`{colors.muted-on-dark}` — #cccccc): Secondary copy on dark tiles.

### Hairlines
- **Hairline** (`{colors.hairline}` — #e0e0e0): 1px border on utility cards.

## Typography

### Font Family
- **Display / Body**: `system-ui, -apple-system, "Noto Sans KR", sans-serif`
- **Code**: `"JetBrains Mono", "Source Code Pro", monospace`

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 48px | 600 | 1.07 | -0.5px | 메인 히어로 헤드라인 |
| `{typography.display-lg}` | 36px | 600 | 1.10 | -0.3px | 포스트 제목, 섹션 타이틀 |
| `{typography.display-md}` | 28px | 600 | 1.20 | -0.2px | 서브 섹션 헤드 |
| `{typography.tagline}` | 19px | 400 | 1.4 | 0 | 서브 카피 |
| `{typography.body}` | 17px | 400 | 1.6 | -0.2px | 본문 단락 |
| `{typography.body-strong}` | 17px | 600 | 1.6 | -0.2px | 강조 본문 |
| `{typography.caption}` | 14px | 400 | 1.43 | -0.1px | 날짜, 태그, 보조 텍스트 |
| `{typography.nav-link}` | 13px | 400 | 1.0 | -0.1px | 네비게이션 링크 |
| `{typography.code}` | 14px | 400 | 1.6 | 0 | 코드 블록 |

### Principles
- 본문은 반드시 17px. 16px을 쓰지 않는다.
- 헤드라인에 negative letter-spacing 필수.
- weight 500 없음 — 400 / 600만 사용.
- 색상 강조 없이 weight와 size로만 위계를 표현.

## Layout

### Spacing System
- **Base unit:** 8px.
- **Tokens:** `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 17px · `{spacing.lg}` 24px · `{spacing.xl}` 40px · `{spacing.xxl}` 64px · `{spacing.section}` 80px.

### Grid & Container
- **Max content width:** 800px (블로그 본문), 1200px (목록 페이지).
- 단일 중앙 컬럼. 좌우 여백은 breathing room.

### Whitespace Philosophy
여백이 콘텐츠의 받침대다. 섹션 위아래 최소 64px. 카드 내부 패딩 24px.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | 전체 배경 섹션 |
| Soft hairline | 1px `{colors.hairline}` | 카드 테두리 |
| Backdrop blur | `backdrop-filter: blur(20px)` + 80% opacity | sticky 헤더 |

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.sm}` | 8px | 인라인 코드, 유틸리티 버튼 |
| `{rounded.md}` | 12px | 카드 |
| `{rounded.lg}` | 18px | 큰 카드 |
| `{rounded.pill}` | 9999px | 태그, CTA 버튼, 뱃지 |

## Do's and Don'ts

### Do
- 모든 인터랙티브 요소는 `{colors.primary}` (#0066cc) 단 하나.
- 헤드라인에 negative letter-spacing 적용.
- 본문은 17px / 400 / 1.6.
- 섹션 구분은 배경색 변경(white ↔ parchment ↔ dark)으로만.
- pill 버튼은 CTA와 태그에만.

### Don't
- 두 번째 accent 색상 추가 금지.
- 카드, 버튼, 텍스트에 shadow 금지.
- 장식적 gradient 금지.
- weight 500 사용 금지.
- serif 폰트 사용 금지.
