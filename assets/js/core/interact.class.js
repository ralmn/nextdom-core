/* This file is part of Jeedom.
 *
 * Jeedom is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Jeedom is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Jeedom. If not, see <http://www.gnu.org/licenses/>.
 */


nextdom.interact = function () {
};

nextdom.interact.remove = function (queryParams) {
  nextdom.private.simpleAjaxWithRequiredParams('Interact', 'remove', queryParams, ['id']);
};


nextdom.interact.get = function (queryParams) {
  nextdom.private.simpleAjaxWithRequiredParams('Interact', 'byId', queryParams, ['id']);
};

nextdom.interact.save = function (queryParams) {
  var paramsRequired = ['interact'];
  if (nextdom.private.isValidQuery(queryParams, paramsRequired)) {
    var params = $.extend({}, nextdom.private.defaultqueryParams, queryParams || {});
    var ajaxParams = nextdom.private.getAjaxParams(params, 'Interact', 'save');
    ajaxParams.data['interact'] = json_encode(queryParams.interact);
    $.ajax(ajaxParams);
  }
};

nextdom.interact.regenerateInteract = function (queryParams) {
  nextdom.private.simpleAjax('Interact', 'regenerateInteract', queryParams);
};

nextdom.interact.execute = function (queryParams) {
  nextdom.private.simpleAjaxWithRequiredParams('Interact', 'execute', queryParams, ['query']);
};