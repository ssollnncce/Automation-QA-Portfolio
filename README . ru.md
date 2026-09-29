# QA Portfolio: Auth / Transfers / Payments (ParaBank)

О проекте

Учебный портфолио-проект QA-инженера: ручное тестирование (тест-дизайн, тест-кейсы, баг-репорты) и автоматизация (API, UI, mobile) для банковского домена — регистрация/логин (Auth), перевод средств (Transfers), оплата счетов (Payments).

Цель проекта — продемонстрировать полный цикл работы QA: от анализа фичи и составления тест-кейсов до автоматизации регрессионных проверок и настройки CI.

Тестируемые цели
Web (UI + API): ParaBank — демо-приложение онлайн-банкинга
Mobile: Sauce Labs My Demo App — демо-приложение для практики Appium
Стек
Слой	Инструменты
Test runner	Pytest
API-тесты	Requests
UI-тесты	Selenium, Page Object Model
Mobile-тесты	Appium, Appium-Python-Client, UiAutomator2
CI	GitHub Actions
Отчётность	Allure
Структура проекта
qa-portfolio/
├── docs/
│   ├── test-plan.md          # тест-план: объём, риски, стратегия
│   └── test-cases/           # ручные тест-кейсы (тест-дизайн техники)
│       ├── auth.md
│       ├── transfers.md
│       └── payments.md
├── bug-reports/              # найденные баги: repro steps, expected/actual, логи
├── tests/
│   ├── api/
│   ├── ui/
│   └── mobile/
├── pages/                    # Page Object классы (UI и mobile)
├── api_clients/               # обёртки над HTTP-запросами
├── conftest.py                # фикстуры pytest
├── pytest.ini
├── requirements.txt
└── README.md
Как запустить
bash
# 1. Клонировать репозиторий и перейти в папку проекта
git clone https://github.com/<username>/qa-portfolio.git
cd qa-portfolio

# 2. Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Запустить тесты по группам (маркеры зарегистрированы в pytest.ini)
pytest -m api -v       # только API-тесты
pytest -m ui -v        # только UI-тесты
pytest -m mobile -v    # только mobile-тесты (требует запущенный Appium Server + эмулятор)
Подход к тест-дизайну

Перед написанием автотестов каждая фича сначала разбирается вручную: определяются пользовательские сценарии, применяются техники тест-дизайна (эквивалентное разбиение, анализ граничных значений, таблицы принятия решений), результат фиксируется в docs/test-cases/. Автоматизация покрывает наиболее критичные и часто повторяющиеся сценарии из этого набора, а не пишется "с нуля" в коде.

Статус
 Каркас проекта, venv, pytest.ini, conftest.py
 Тест-дизайн и тест-кейсы: Auth
 Тест-дизайн и тест-кейсы: Transfers
 Тест-дизайн и тест-кейсы: Payments
 API-автоматизация (ParaBank)
 UI-автоматизация (ParaBank, POM)
 Mobile-автоматизация (Appium)
 Найденные баги задокументированы
 CI (GitHub Actions)
 Allure-отчёт