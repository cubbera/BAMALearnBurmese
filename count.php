<?php

header('Content-Type: application/json');

$file = __DIR__ . '/data/download-counts.json';

$allowed = [
    '33-consonants',
    'scripts-cheatsheet',
    'suffixes-cheatsheet',
    'stroke-order',
    'mac-keyboard'
];

$item = $_GET['item'] ?? '';

if (!in_array($item, $allowed, true)) {
    http_response_code(400);
    echo json_encode([
        'error' => 'Invalid item'
    ]);
    exit;
}

if (!file_exists($file)) {
    file_put_contents($file, '{}');
}

$counts = json_decode(
    file_get_contents($file),
    true
);

if (!is_array($counts)) {
    $counts = [];
}

if (!isset($counts[$item])) {
    $counts[$item] = 0;
}

$counts[$item]++;

file_put_contents(
    $file,
    json_encode($counts, JSON_PRETTY_PRINT),
    LOCK_EX
);

echo json_encode([
    'item' => $item,
    'count' => $counts[$item]
]);

?>