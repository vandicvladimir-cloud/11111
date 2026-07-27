from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Услуги спецтехники | Столин и Столинский район</title>

<!-- Google Font -->
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>
:root {
    --bg-color: #f8fafc;
    --card-bg: #ffffff;
    --border-color: #e2e8f0;
    --accent: #f59e0b;
    --accent-hover: #d97706;
    --accent-glow: rgba(245, 158, 11, 0.25);
    --text-main: #0f172a;
    --text-muted: #64748b;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: var(--bg-color);
    color: var(--text-main);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

header {
    text-align: center;
    padding: 50px 20px 20px;
}

.badge {
    display: inline-block;
    padding: 6px 16px;
    background: #fef3c7;
    border: 1px solid #fde68a;
    color: #b45309;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
    text-transform: uppercase;
}

header h1 {
    font-size: clamp(28px, 5vw, 44px);
    font-weight: 800;
    color: var(--text-main);
    letter-spacing: -0.5px;
}

header p {
    color: var(--text-muted);
    font-size: 16px;
    margin-top: 8px;
    font-weight: 500;
}

.container {
    max-width: 900px;
    width: 100%;
    margin: 0 auto;
    padding: 20px;
}

/* Карточки */
.card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    padding: 32px;
    margin-bottom: 24px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
}

/* Блок связи */
.cta-card {
    text-align: center;
    border: 2px solid #fde68a;
    background: linear-gradient(180deg, #fffbeb 0%, #ffffff 100%);
}

.cta-card h2 {
    font-size: 18px;
    color: var(--text-muted);
    font-weight: 600;
    margin-bottom: 12px;
}

.phone-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    background: linear-gradient(135deg, var(--accent), var(--accent-hover));
    color: #ffffff;
    font-size: clamp(22px, 4vw, 30px);
    font-weight: 800;
    text-decoration: none;
    padding: 16px 36px;
    border-radius: 16px;
    margin: 8px 0;
    box-shadow: 0 10px 20px var(--accent-glow);
    transition: all 0.25s ease;
}

.phone-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 28px var(--accent-glow);
}

.cta-subtext {
    font-size: 14px;
    color: var(--text-muted);
    margin-top: 8px;
}

/* Таблица прайс-листа */
.section-title {
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 20px;
    color: var(--text-main);
}

.table-wrapper {
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th {
    background: #f1f5f9;
    color: var(--text-muted);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 14px 18px;
    text-align: left;
    font-weight: 700;
    border-radius: 8px;
}

td {
    padding: 18px;
    border-bottom: 1px solid var(--border-color);
    font-size: 15px;
}

tr:last-child td {
    border-bottom: none;
}

tr:hover td {
    background: #f8fafc;
}

.tech-name {
    font-weight: 700;
    color: var(--text-main);
}

.tech-desc {
    color: var(--text-muted);
    line-height: 1.5;
}

footer {
    text-align: center;
    padding: 24px;
    color: var(--text-muted);
    font-size: 13px;
    border-top: 1px solid var(--border-color);
    background: #ffffff;
}
</style>
</head>

<body>

<div>
    <header>
        <span class="badge">📍 Столин и Столинский район</span>
        <h1>Услуги спецтехники</h1>
        <p>Надёжная техника для любых задач</p>
    </header>

    <div class="container">

        <!-- Карточка связи -->
        <div class="card cta-card">
            <h2>Быстрый заказ и консультация</h2>
            <a href="tel:+375295448899" class="phone-btn">
                <span>📞</span> +375 (29) 544-88-99
            </a>
            <p class="cta-subtext">Звоните прямо сейчас — подберем технику и согласуем время</p>
        </div>

        <!-- Прайс-лист -->
        <div class="card">
            <h2 class="section-title">🚜 Прайс-лист работ</h2>
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Техника / Услуга</th>
                            <th>Описание и возможности</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="tech-name">Телескопический погрузчик</td>
                            <td class="tech-desc">Грузоподъемность 3–4 т, вылет стрелы 13–16 м</td>
                        </tr>
                        <tr>
                            <td class="tech-name">Мини-экскаватор</td>
                            <td class="tech-desc">Копка траншей, работа в стесненных условиях и на сложных участках</td>
                        </tr>
                        <tr>
                            <td class="tech-name">Трал</td>
                            <td class="tech-desc">Перевозка негабаритной техники и оборудования</td>
                        </tr>
                        <tr>
                            <td class="tech-name">Самосвал</td>
                            <td class="tech-desc">Объем 20 м³, доставка сыпучих грузов, вывоз грунта и мусора</td>
                        </tr>
                        <tr>
                            <td class="tech-name">Вольво с манипулятором</td>
                            <td class="tech-desc">Грузоподъемность борта 6 т, манипулятор 1.5 т</td>
                        </tr>
                        <tr>
                            <td class="tech-name">Автовышка</td>
                            <td class="tech-desc">Высотные работы до 25 метров</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

    </div>
</div>

<footer>
    © 2026 Услуги спецтехники | Столин и Столинский район
</footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)