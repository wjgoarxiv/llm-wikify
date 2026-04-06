<p align="center"><img src="./cover.png" width="100%" /></p>

<h1 align="center">llm-wikify</h1>
<p align="center">
  <em>거대한 범용 볼트를 만들지 않고, 현재 작업 디렉터리를 작고 누적되는 LLM 위키로 바꿉니다.</em>
</p>
<p align="center">
  <a href="#언제-써야-하나">언제 써야 하나</a> · <a href="#빠른-시작">빠른 시작</a> · <a href="#기능">기능</a> · <a href="#워크플로우">워크플로우</a> · <a href="#리포지토리-구성">리포지토리 구성</a> · <a href="./README.md">English</a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/skill-local%20wiki-blueviolet" />
  <img src="https://img.shields.io/badge/format-markdown-green" />
  <img src="https://img.shields.io/badge/scope-task--local-orange" />
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20OpenCode-black" />
</p>

---

> [!NOTE]
> `llm-wikify`는 Karpathy의 `llm-wiki` 아이디어에서 출발했지만, **작업 중심(task-driven)** 흐름에 맞게 좁혀 설계했습니다. 하나의 거대한 메가 위키를 계속 뒤지는 대신, **현재 작업 디렉터리 자체를 미니 위키 경계**로 삼습니다. `raw/`에 들어온 새 자료는 이 로컬 마크다운 지식베이스로 점진적으로 통합되고, 프로젝트가 바뀌면 위키 경계도 함께 바뀝니다.

## 왜 필요한가

Karpathy의 핵심 통찰은 매우 강력합니다. 질문할 때마다 원문 문서를 다시 긁어모으는 대신, LLM이 지속적으로 위키를 유지하게 만들면 지식이 누적됩니다.

하지만 실제 엔지니어링, 리서치, 실사, 프로젝트 문서화에서는 범용 거대 위키가 금방 시끄러워집니다. `llm-wikify`는 그 범위를 **현재 활성 리포지토리 또는 작업 폴더**로 줄여서 더 실용적인 기본값을 제공합니다.

그 결과:

- 위키 표면적이 작아지고
- 사람과 에이전트가 더 빨리 탐색할 수 있으며
- 출처 추적과 유지보수가 쉬워지고
- 새 자료를 현재 프로젝트에 맞게 더 깔끔하게 흡수할 수 있고
- 모든 것을 개인 PKM 제국으로 과도하게 일반화할 유혹이 줄어듭니다

## 기능

- **작업-로컬 위키 경계** — 사용자가 범위를 넓히지 않는 한 작업 디렉터리 자체를 위키로 간주
- **부트스트랩 모드** — 위키가 없으면 MECE에 가깝고 작은 구조를 자동으로 생성
- **인제스트 모드** — `raw/`의 자료를 읽고 source page, topic page, index에 통합
- **유지보수 모드** — 오래된 페이지, 깨진 링크, orphan, 중복, 약한 내비게이션 점검
- **출처 우선 워크플로우** — 근거 없는 요약 덩어리가 아니라 출처와 함께 지식 보존
- **최소 구조 편향** — 현재 프로젝트가 정당화하는 폴더와 페이지만 생성
- **근거 명시 요구** — durable page는 어떤 repo landmark / source note / raw input에서 왔는지 밝혀야 함
- **멱등적 인제스트 편향** — 같은 소스를 다시 넣어도 중복 페이지 대신 기존 노트를 업데이트
- **지식 누적** — 가치 있는 질의 응답 결과를 채팅에만 남기지 않고 위키로 환원 가능

## 언제 써야 하나

다음 상황에서 `llm-wikify`를 쓰면 좋습니다:

- 리포지토리나 작업 디렉터리를 지속적인 마크다운 지식베이스로 만들고 싶을 때
- 새 source file, note, URL, export, transcript를 `raw/`에 넣고 흡수하고 싶을 때
- 세션이 바뀌어도 프로젝트 이해를 안정적으로 누적하고 싶을 때
- 리서치, 엔지니어링, 실사, 계획, 문서화 작업을 위한 작은 로컬 위키가 필요할 때
- 이미 있는 로컬 위키를 건강검진하고 정리하고 싶을 때

반대로 이런 경우에는 과합니다:

- 일회성 요약만 필요할 때
- 일반적인 markdown 정리만 할 때
- 개인 전체 vault를 재설계하려 할 때
- 여러 무관한 프로젝트를 하나의 PKM 체계로 묶으려 할 때

## 빠른 시작

### 1. LLM용 빠른 스킬 설치

> [!TIP]
> 셸 명령을 실행할 수 있는 LLM 에이전트라면, 아래 코드블록을 그대로 복사해서 채팅에 붙여넣는 것만으로 스킬 설치를 자동으로 끝낼 수 있습니다.

```text
llm-wikify 스킬을 설치해줘.
1. git clone https://github.com/wjgoarxiv/llm-wikify /tmp/llm-wikify
2. mkdir -p ~/.claude/skills/llm-wikify
3. cp -r /tmp/llm-wikify/SKILL.md /tmp/llm-wikify/assets /tmp/llm-wikify/evals ~/.claude/skills/llm-wikify/
4. cp /tmp/llm-wikify/generate_cover.sh ~/.claude/skills/llm-wikify/
5. chmod +x ~/.claude/skills/llm-wikify/generate_cover.sh
6. Test: test -f ~/.claude/skills/llm-wikify/SKILL.md && echo "OK: llm-wikify installed"
7. "llm-wikify installed successfully"라고 말해줘
```

다른 도구에서는 skills 경로만 바꾸면 됩니다:

- Codex CLI: `~/.codex/skills/llm-wikify/`
- OpenCode: `~/.config/opencode/skills/llm-wikify/`
- Gemini CLI: `~/.gemini/skills/llm-wikify/`

### 2. 소스 자료를 `raw/`에 넣기

예시:

- 클리핑한 아티클
- markdown으로 변환한 PDF
- 회의 노트
- 인터뷰 transcript
- 복사한 문서
- LLM이 읽어야 할 URL

### 3. 에이전트에게 현재 디렉터리를 위키화하라고 요청하기

예시 프롬프트:

```text
이 작업 디렉터리를 작은 로컬 위키로 바꿔줘.
지금 필요한 최소 구조만 부트스트랩해.
```

```text
raw/ 안의 파일들을 이 프로젝트 위키로 인제스트해.
출처는 보존하고, 거대한 요약 한 파일로 뭉개지 마.
```

```text
이 디렉터리의 위키를 lint / maintain 해줘.
안전한 수정만 적용하고, 짧은 maintenance report를 남겨줘.
```

### 4. 위키를 누적시키기

시간이 지나면 에이전트는 다음을 계속 갱신해야 합니다:

- `wiki/home.md`
- `wiki/index.md`
- topic page
- source note
- maintenance log

원문은 raw에 남고, 위키는 유지되는 합성 레이어가 됩니다.

## 워크플로우

### Bootstrap

위키가 아직 없다면, `llm-wikify`는 다음을 해야 합니다:

1. 현재 디렉터리를 먼저 조사
2. 기존 문서를 중복 작성하지 말고 필요시 링크로 보존
3. 최소 폴더 구조 생성
4. `home.md`, `index.md`, 몇 개의 grounded page 작성
5. `schema/wiki-rules.md`에 로컬 규칙과 경계 기록

### Ingest

`raw/`에 새 자료가 들어오면:

1. 소스를 읽고
2. source note를 생성 또는 업데이트하고
3. 관련 topic/entity page를 업데이트하며
4. 근거가 약하거나 부분적인 내용은 uncertainty를 표시하고
5. `log/log.md`에 인제스트 기록을 남깁니다

### Query

사용자가 프로젝트 질문을 하면:

1. `wiki/index.md`를 먼저 읽고
2. 관련 로컬 페이지를 따라간 뒤
3. 유지된 위키를 바탕으로 답변하고
4. 오래 남길 가치가 있는 분석이면 다시 위키에 파일링합니다

### Lint / maintain

주기적으로 다음을 점검해야 합니다:

- stale page
- broken link
- orphan page
- duplicate topic
- inconsistent naming
- weak summary
- raw-ingestion leftover

그 후 안전한 수정만 적용하고 maintenance report를 남깁니다.

깔끔해 보이는 index와 report만 늘어놓고 실제 정리를 하지 않는 방식으로 통과하면 안 됩니다.

## 리포지토리 구성

```text
llm-wikify/
├── SKILL.md
├── README.md
├── README-ko.md
├── cover.png
├── generate_cover.sh
├── assets/
│   ├── home-template.md
│   ├── maintenance-report-template.md
│   ├── source-note-template.md
│   └── wiki-rules-template.md
└── evals/
    └── evals.json
```

## 위키화된 프로젝트의 기본 폴더 계약

기본 목표 구조는 의도적으로 작습니다:

```text
raw/
wiki/
  home.md
  index.md
  topics/
  entities/
  sources/
schema/
  wiki-rules.md
log/
  log.md
```

이건 **출발점**이지 강제 규칙이 아닙니다. 프로젝트가 더 작은 구조를 요구하면 더 적게 만들어야 합니다.

## 설계 원칙

### 1. Local first
프로젝트 디렉터리가 지식 경계입니다.

### 2. Incremental over regenerative
새 소스가 들어오면 관련 페이지를 갱신하고, 기본적으로 전체를 재생성하지 않습니다.

### 3. Provenance over vibes
중요한 주장에는 source note 또는 raw material로 돌아갈 수 있는 경로가 있어야 합니다.

### 4. Navigation over volume
페이지 수를 늘리는 것보다 들어가고 따라가기 쉬운 구조가 더 중요합니다.

### 5. Maintenance is the product
새 자료가 계속 들어와도 위키가 깨지지 않도록 유지하는 것 자체가 핵심 가치입니다.

## 영감

이 스킬은 Karpathy의 `llm-wiki` 아이디어 — 원문 chunk를 매번 다시 찾는 대신, 모델이 유지하는 지속적 위키 — 에 직접적으로 영감을 받았습니다.

`llm-wikify`는 이를 더 실무적인 기본값으로 줄입니다: **하나의 작업 디렉터리, 하나의 유지되는 미니 위키**.

## 검증

이 리포지토리에는 `evals/evals.json`에 세 가지 압박형 프롬프트가 들어 있습니다:

- 지저분한 repo에서 로컬 위키를 부트스트랩하기
- `raw/`의 혼합 자료를 인제스트하기
- 하나의 파일로 납작하게 만들지 않고 진화하는 위키를 유지보수하기

이 테스트들은 “그럴듯한 말은 하지만 실제로는 generic agent와 큰 차이가 없는” 실패를 잡기 위해 설계되었습니다.
