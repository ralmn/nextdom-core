<?php
if (!isConnect()) {
    throw new Exception('{{401 - Accès non autorisé}}');
}
?>
<div id="div_alertObjectSummary"></div>
<table class="table table-bordered table-condensed tablesorter" id="table_ObjectSummary">
    <thead>
        <tr>
            <th style="cursor:default">{{ID}}</th>
            <th style="cursor:default">{{Objet}}</th>
            <th style="cursor:default">{{Père}}</th>
            <th style="cursor:default" data-sorter="false" data-filter="false">{{Visible}}</th>
            <th style="cursor:default" data-sorter="false" data-filter="false">{{Masqué}}</th>
            <th style="cursor:default" data-sorter="false" data-filter="false">{{Résumé Défini}} <sup style="cursor:default" title="Si grisé, alors il n'est pas remonté en résumé global">?</th>
                <th style="cursor:default" data-sorter="false" data-filter="false">{{Résumé Dashboard Masqué}}</th>
                <th style="cursor:default" data-sorter="false" data-filter="false">{{Résumé Mobile Masqué}}</th>
            </tr>
        </thead>
        <tbody>
            <?php
$allObject = jeeObject::buildTree(null, false);
foreach ($allObject as $object) {
    echo '<tr class="tr_object" data-object_id="' . $object->getId() . '"><td><span class="label label-info txtSizeNormal">' . $object->getId() . '</span></td>';
    echo '<td>';
    for ($i = 0; $i < $object->getConfiguration('parentNumber'); $i++) {
        echo '&nbsp;&nbsp;&nbsp;';
    }
    echo '<span style="font-size : 1.3em;">' . $object->getHumanName(true, true) . '</span>';
    echo '</td>';
    $father = $object->getFather();
    if ($father) {
        echo '<td><span class="txtSizeNormal">' . $father->getHumanName(true, true) . '</span></td>';
    } else {
        echo '<td><span class="label label-info txtSizeNormal"></span></td>';
    }
    if ($object->getIsVisible()) {
        echo '<td><span class="label label-success txtSizeNormal" title="{{Oui}}"><i class="fas fa-check"></i></span></td>';
    } else {
        echo '<td><span class="label label-danger txtSizeNormal" title="{{Non}}"><i class="fas fa-times"></i></span></td>';
    }
    if ($object->getConfiguration("hideOnDashboard", 0) == 1) {
        echo '<td><span class="label label-success txtSizeNormal" title="{{Oui}}"><i class="fas fa-check"></i></span></td>';
    } else {
        echo '<td><span class="label label-danger txtSizeNormal" title="{{Non}}"><i class="fas fa-times"></i></span></td>';
    }
    echo '<td>';
    foreach (config::byKey('object:summary') as $key => $value) {
        $title = '';
        if (!isset($object->getConfiguration('summary')[$key]) || !is_array($object->getConfiguration('summary')[$key]) || count($object->getConfiguration('summary')[$key]) == 0) {
            continue;
        }
        foreach ($object->getConfiguration('summary')[$key] as $summary) {
            if (cmd::byId(str_replace('#', '', $summary['cmd']))) {
                $title .= '&#10;' . cmd::byId(str_replace('#', '', $summary['cmd']))->getHumanName();
            } else {
                $title .= '&#10;' . $summary['cmd'];
            }
        }
        if (count($object->getConfiguration('summary')[$key]) > 0) {
            if ($object->getConfiguration('summary::global::' . $key) == 1) {
                echo '<a style="cursor:default;text-decoration:none;" title="' . $value['name'] . $title . '">' . $value['icon'] . '<sup> ' . count($object->getConfiguration('summary')[$key]) . '</sup></a>  ';
            } else {
                echo '<a style="cursor:default;color:grey;text-decoration:none;" title="' . $value['name'] . $title . '">' . $value['icon'] . '<sup> ' . count($object->getConfiguration('summary')[$key]) . '</sup></a>  ';
            }
        }
    }
    echo '</td>';
    echo '<td>';
    foreach (config::byKey('object:summary') as $key => $value) {
        if ($object->getConfiguration('summary::hide::desktop::' . $key) == 1) {
            echo '<a style="cursor:default;text-decoration:none;" title="' . $value['name'] . '">' . $value['icon'] . '</a>  ';
        }
    }
    echo '</td>';
    echo '<td>';
    foreach (config::byKey('object:summary') as $key => $value) {
        if ($object->getConfiguration('summary::hide::mobile::' . $key) == 1) {
            echo '<a style="cursor:default;text-decoration:none;" title="' . $value['name'] . '">' . $value['icon'] . '</a>  ';
        }
    }
    echo '</td>';
}
?>
        </tbody>
    </table>

    <script>
        initTableSorter();

        $("#table_ObjectSummary").sortable({
            axis: "y",
            cursor: "move",
            items: ".tr_object",
            placeholder: "ui-state-highlight",
            tolerance: "intersect",
            forcePlaceholderSize: true,
            stop: function (event, ui) {
                var objects = [];
                $('#table_ObjectSummary .tr_object').each(function () {
                    objects.push($(this).attr('data-object_id'));
                });
                nextdom.object.setOrder({
                    objects: objects,
                    error: function (error) {
                        $('#div_alertObjectSummary').showAlert({message: error.message, level: 'danger'});
                    }
                });
            }
        });
    </script>
