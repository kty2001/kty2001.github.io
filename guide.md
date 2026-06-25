# 주간회고 작성 가이드

## 목적

지난 일주일을 돌아보고, 더 나은 다음 주를 만들기 위한 기록이다.
완벽한 글을 쓰는 것이 목표가 아니다. 빠르게 작성하고 꾸준히 쌓는 것이 중요하다.

---

## 새 주차 포스트 작성 순서

### 1. 이전 파일 복사

```
posts/week1.html → posts/week2.html
```

VS Code에서 복사하거나 터미널에서:

```bash
cp posts/week1.html posts/week2.html
```

### 2. 메타 정보 수정

`week2.html` 상단 3곳 수정:

```html
<title>Week 2 주간회고 · kty2001</title>

<span class="post-tag">Week 2</span>
<span class="post-date-detail">2026년 06월 24일 — 06월 28일</span>

<h1>이번 주 제목</h1>
```

### 3. 본문 내용 작성

아래 섹션 순서대로 채운다.

| 섹션 | 클래스 | 내용 |
|---|---|---|
| 이번 주 학습 내용 | `block` | 챕터별 `sub-block`으로 나눠 작성 |
| KPT 회고 | `block` > `kpt-section` × 3 | Keep / Problem / Try 순서 |
| 새롭게 발견한 것 | `block` | 인상적이었던 개념, 코드 예시 포함 가능 |
| 트러블슈팅 | `block` > `trouble-card` | 발생한 에러, 원인, 수정 전/후 코드 |
| 다음 주 목표 | `block` > `ul` | 3개 내외 |
| 마무리 한마디 | `closing-quote` | 한두 문장, 스스로를 다독이는 말 |

트러블슈팅이 없는 주차는 해당 섹션을 삭제해도 된다.

### 4. index.html에 링크 추가

`index.html`의 포스트 목록 맨 위에 추가 (최신순):

```html
<a href="posts/week2.html" class="post-item">
  <div class="post-item-left">
    <span class="post-week">Week 2</span>
    <span class="post-title">이번 주 제목</span>
  </div>
  <span class="post-date">2026.06.24 — 06.28</span>
</a>
```

### 5. 커밋 & 배포

```bash
git add .
git commit -m "Add week2"
git push origin main
```

배포 후 `https://kty2001.github.io` 에서 확인 (반영까지 1~2분 소요).

---

## 섹션별 작성 팁

### 이번 주 학습 내용

챕터 단위로 `sub-block`을 나눈다. 개념 설명과 함께 헷갈렸던 부분이나 흥미로웠던 동작 방식을 짧게 적는다.

```html
<div class="sub-block">
  <h3 class="sub-block-title">01. 챕터명</h3>
  <p>간단한 요약</p>
  <ul>
    <li><code>키워드</code> — 설명</li>
  </ul>
</div>
```

### KPT 회고

- **Keep** — 잘 됐던 것, 계속할 것
- **Problem** — 아쉬웠던 것, 반복된 실수
- **Try** — Problem에 대한 구체적인 해결책

```html
<div class="kpt-section">
  <h3 class="kpt-section-title">Keep</h3>
  <p>내용</p>
</div>
```

### 트러블슈팅

에러 메시지, 원인 분석, 수정 전/후 코드를 함께 기록한다.
코드 블록은 `<div class="code-block"><code>` 사용.

```html
<div class="trouble-card">
  <p class="trouble-card-title">문제 : 에러 제목</p>
  <p>상황 설명</p>
  <div class="code-block"><code>수정 전 코드</code></div>
  <p>원인 설명</p>
  <div class="code-block"><code>수정 후 코드</code></div>
  <p>배운 점</p>
</div>
```

---

## 회고 방법론 참고

**KPT** (이 블로그의 기본 형식)
- Keep / Problem / Try

**PMI**
- Plus / Minus / Impressive

**The four Fs**
- Facts / Feelings / Findings / Future

방법론에 얽매이지 말고, 쓰다 보면 자연스럽게 자기만의 형식이 생긴다.
