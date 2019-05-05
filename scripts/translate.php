<?php

if (count($argv) == 1) {
    printf("usage: %s file1 [file2] [file...]\n", $argv[0]);
    exit(1);
}

require (__DIR__.'/../vendor/autoload.php');

use Symfony\Component\Translation\Translator;
use Symfony\Component\Translation\Loader\YamlFileLoader;

function translateFile($target, $translator) {
    if (false === file_exists($target)) {
        return;
    }

    $content = file_get_contents($target);
    preg_match_all("/{{(.*?)}}/s", $content, $matches);
    $translationArray = [];
    foreach ($matches[1] as $toTranslate) {
        $translation = $translator->trans($toTranslate);
        if ($translation == '') {
            $translation = $toTranslate;
        }
        $translationArray['{{'.$toTranslate.'}}'] = $translation;
    }
    $result = str_replace(array_keys($translationArray), $translationArray, $content);
    file_put_contents($target, $result);
}


$translator = new Translator('fr_FR', null, __DIR__.'/../var/i18n');
$translator->addLoader('yaml', new YamlFileLoader());
$translator->addResource('yaml', '../translations/fr_FR.yml', 'fr_FR');

array_shift($argv);
foreach ($argv as $target) {
    translateFile($target, $translator);
}
