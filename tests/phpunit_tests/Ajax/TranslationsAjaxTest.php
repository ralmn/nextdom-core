<?php

/* This file is part of NextDom Software.
 *
 * NextDom is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NextDom Software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NextDom Software. If not, see <http://www.gnu.org/licenses/>.
 *
 * @Support <https://www.nextdom.org>
 * @Email   <admin@nextdom.org>
 * @Authors/Contributors: Sylvaner, Byackee, cyrilphoenix71, ColonelMoutarde, edgd1er, slobberbone, Astral0, DanoneKiD
 */


use NextDom\Ajax\CronAjax;

require_once('BaseAjaxTest.php');

class TranslationsAjaxTest extends BaseAjaxTest
{


    /**
     * @var CronAjax
     */
    private $cronAjax;

    public function setUp()
    {
        $this->cronAjax = new CronAjax();
    }

    public function tearDown()
    {
        $this->cleanGetParams();
    }

    public function testGetTranslations()
    {
       return true;
    }

}
