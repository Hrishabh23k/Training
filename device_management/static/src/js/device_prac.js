/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';

export class DeviceController extends ListController{
    setup(){
        super.setup()
    }
    OnTestClick(){
        console.log("Test button run successfully!!!!!")
    }
}


registry.category('views').add('Device'{
   ...listView,
   Controller: DeviceController,
   buttonTemplate: "device_management.s.button",
});