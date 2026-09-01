# Product Research Synthesis Suite

Один orchestration-skill для полного продуктового разбора:

- сырые количественные данные;
- интервью, заметки, support/sales feedback;
- краткий контекст продукта;
- мысли и предположения автора;
- исходные гипотезы;
- цели и метрики;
- результаты A/B-тестов;
- итог: выводы, противоречия, дыры, изменения картины мира и следующие шаги.

## Почему это не один огромный SKILL.md

Большой монолит расходует контекст ещё до начала анализа. Здесь основной skill
маленький и использует **progressive disclosure**:

1. сначала классифицирует входные материалы;
2. загружает только правила текущего этапа;
3. обрабатывает исходники пакетами;
4. сохраняет компактный evidence ledger;
5. объединяет количественные и качественные выводы только после независимого
   анализа;
6. формирует широкий отчёт с приложениями, не удерживая все сырые материалы в
   активном контексте.

Upstream-правила не переписаны. Пять исходных репозиториев подключены как
submodules и закреплены на конкретных commit SHA. Файл `SOURCES.lock.json`
определяет, какие оригинальные файлы допустимо загружать для каждой задачи.

## Главный skill

`skills/product-research-synthesis/SKILL.md`

Он самостоятельно маршрутизирует работу между:

- Clamp: диагностика метрик, funnels, cohorts, anomalies, causal checks,
  experiments;
- Borghei: North Star, metric tree, instrumentation, retention tooling;
- RampStack: качественный research synthesis, analytics setup/strategy, OKR;
- Alireza Rezvani: research discipline и детерминированные Python-утилиты;
- GrowthBook: дизайн и интерпретация экспериментов.

## Установка

```bash
git clone --recurse-submodules --branch product-research-suite \
  https://github.com/heteraff1-tech/analytics-skills.git
cd analytics-skills
python3 scripts/validate_bundle.py
```

Если репозиторий уже клонирован:

```bash
git submodule update --init --recursive
```

Если среда не инициализирует submodules, основной skill использует
`SOURCES.lock.json`, чтобы открыть тот же оригинальный файл по закреплённому
commit в GitHub.

## Рекомендуемая структура материалов

```text
input/
├── project-brief.md
├── thinking.md
├── goals.csv
├── hypotheses.csv
├── quantitative/
│   ├── events.csv
│   ├── funnel.csv
│   └── retention.csv
├── interviews/
│   ├── P01.md
│   ├── P02.md
│   └── P03.md
└── experiments/
    └── checkout-test.json
```

Создать заготовку:

```bash
python3 scripts/prepare_run.py my-study
```

## Запуск

Пример запроса:

> Используй `product-research-synthesis` в full mode. Проанализируй все
> материалы в `input/`. Сначала независимо разбери данные, интервью и мои мысли,
> затем сведи их. Покажи исходные и новые гипотезы, что подтвердилось или
> изменилось, где противоречия и дыры, как пересмотреть цели и какие проверки
> провести дальше. Глубина: standard.

Доступные уровни: `compact`, `standard` и `deep`. По умолчанию используется
`standard`; `deep` расширяет отчёт, но не отменяет поэтапную загрузку.

## Лицензии

Оркестратор и вспомогательные файлы этого репозитория — MIT. Upstream-компоненты
остаются под собственными лицензиями. Особое ограничение: `borghei/Claude-Skills`
использует Commons Clause + MIT и не разрешает перепродажу/платный сервис,
ценность которого существенно основана на этих материалах. См.
`THIRD_PARTY_NOTICES.md` и `third_party/licenses/`.
