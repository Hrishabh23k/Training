/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
export class DeviceListController extends ListController {
   setup() {
       super.setup();
   }
   OnTestClick() {
        alert("Hello")
   }
}


registry.category("views").add("button_in_tree", {
   ...listView,
   Controller: DeviceListController,
//   buttonTemplate: "device_management.ListView.Buttons",
});