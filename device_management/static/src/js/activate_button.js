/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";

export class ApprovedController extends ListController{
    setup(){
        super.setup()
        this.orm = useService("orm");
        this.notification = useService('notification');
    }
    OnTestClick(){
        console.log("Test button run successfully!!!!!")
    }
    async approve_button_click(){
//            var result = await this.orm.call(
//                "device.assignment",
//                "button_click",
//                [[]],
//            );
//            console.log(result);
            const record_ids = await this.getSelectedResIds();
            await this.orm.call('device.assignment', 'button_click', [record_ids]).then(() => {
                this.notification.add(
                this.env._t("Your Device Assignment is Approved"),
            )
            });
            console.log(record_ids);
    }

}


registry.category('views').add('approved', {
   ...listView,
   Controller: ApprovedController,
   buttonTemplate: "device_management.activate.button",
});