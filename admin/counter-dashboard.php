<?php

header('Content-Type: text/html; charset=UTF-8');

$file = __DIR__ . '/data/download-counts.json';

$items = [
    'bbe-pdf' => [
        'name' => 'Burmese by Ear PDF',
        'description' => 'John Okell — PDF',
    ],
    'bbe-mp3' => [
        'name' => 'Burmese by Ear Audio',
        'description' => 'John Okell — Audio',
    ],
    '33-consonants' => [
        'name' => 'Burmese Consonants',
        'description' => '33 Consonants',
    ],
    'scripts-cheatsheet' => [
        'name' => 'Basic Scripts Cheatsheet',
        'description' => 'Burmese script / syllable formula',
    ],
    'suffixes-cheatsheet' => [
        'name' => 'Basic Suffixes Cheatsheet',
        'description' => 'Core grammatical suffixes',
    ],
    'stroke-order' => [
        'name' => 'Burmese Script Stroke Order',
        'description' => 'Stroke order reference',
    ],
    'mac-keyboard' => [
        'name' => 'Burmese MacOS Keyboard',
        'description' => 'MacOS keyboard reference',
    ],
];

/*
 * Read the counter data.
 */
$counts = [];

if (file_exists($file)) {
    $json = file_get_contents($file);
    $data = json_decode($json, true);

    if (is_array($data)) {
        $counts = $data;
    }
}

/*
 * Calculate total.
 */
$total = 0;

foreach ($items as $key => $item) {
    $total += (int)($counts[$key] ?? 0);
}

?>
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Counter Dashboard — BAMA Learn Burmese</title>

<style>

:root {
    --ink: #221b16;
    --paper: #f4efe1;
    --paper-2: #eae1c8;
    --jade: #1f5d42;
    --jade-deep: #163f2d;
    --gold: #ab7f28;
    --muted: #5c5240;
    --line: #ddd2ac;
    --white: #fffdf7;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

main {
    max-width: 850px;
    margin: 0 auto;
    padding: 50px 20px 70px;
}

.eyebrow {
    display: block;
    margin-bottom: 8px;
    color: var(--gold);
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

h1 {
    margin: 0 0 8px;
    font-family: Georgia, serif;
    font-size: 38px;
    line-height: 1.2;
    color: var(--jade-deep);
}

.intro {
    margin: 0 0 30px;
    color: var(--muted);
}

/* Total */

.total-box {
    margin-bottom: 30px;
    padding: 25px;
    background: var(--jade);
    color: white;
    border-radius: 12px;
}

.total-label {
    font-size: 13px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    opacity: 0.8;
}

.total-number {
    margin-top: 3px;
    font-family: Georgia, serif;
    font-size: 42px;
    font-weight: bold;
}

/* Counter rows */

.counter-list {
    display: grid;
    gap: 12px;
}

.counter-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;

    padding: 18px 20px;

    background: var(--white);
    border: 1px solid var(--line);
    border-radius: 10px;
}

.counter-info {
    min-width: 0;
}

.counter-name {
    font-weight: bold;
    font-size: 17px;
}

.counter-description {
    color: var(--muted);
    font-size: 13px;
}

.counter-number {
    flex-shrink: 0;

    min-width: 80px;

    text-align: right;

    font-family: Georgia, serif;
    font-size: 27px;
    font-weight: bold;
    color: var(--jade);
}

.counter-number small {
    display: block;
    font-family: Arial, sans-serif;
    font-size: 11px;
    font-weight: normal;
    color: var(--muted);
}

/* Controls */

.controls {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;

    margin-top: 30px;
}

.refresh {
    padding: 10px 16px;

    border: 1px solid var(--jade);
    border-radius: 7px;

    background: transparent;
    color: var(--jade);

    font-size: 14px;
    font-weight: bold;

    cursor: pointer;
}

.refresh:hover {
    background: var(--jade);
    color: white;
}

.updated {
    color: var(--muted);
    font-size: 12px;
}

/* Mobile */

@media (max-width: 600px) {

    main {
        padding-top: 35px;
    }

    h1 {
        font-size: 31px;
    }

    .counter-row {
        padding: 16px;
    }

    .counter-name {
        font-size: 15px;
    }

    .counter-number {
        font-size: 23px;
        min-width: 60px;
    }

    .controls {
        align-items: flex-start;
        flex-direction: column;
    }

}

</style>

</head>

<body>

<main>

    <span class="eyebrow">BAMA Learn Burmese</span>

    <h1>Counter Dashboard</h1>

    <p class="intro">
        View counts for downloads and resources.
    </p>


    <section class="total-box">

        <div class="total-label">
            Total views
        </div>

        <div class="total-number">
            <?= number_format($total) ?>
        </div>

    </section>


    <section class="counter-list">

        <?php foreach ($items as $key => $item): ?>

            <?php $count = (int)($counts[$key] ?? 0); ?>

            <div class="counter-row">

                <div class="counter-info">

                    <div class="counter-name">
                        <?= htmlspecialchars($item['name'], ENT_QUOTES, 'UTF-8') ?>
                    </div>

                    <div class="counter-description">
                        <?= htmlspecialchars($item['description'], ENT_QUOTES, 'UTF-8') ?>
                    </div>

                </div>

                <div class="counter-number">

                    <?= number_format($count) ?>

                    <small>views</small>

                </div>

            </div>

        <?php endforeach; ?>

    </section>


    <div class="controls">

        <div class="updated">
            Updated <?= date('Y-m-d H:i:s') ?>
        </div>

        <button
            class="refresh"
            onclick="location.reload()">
            ↻ Refresh
        </button>

    </div>

</main>

</body>
</html>