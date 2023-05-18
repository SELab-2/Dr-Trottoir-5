import {mount} from "@vue/test-utils"
import AdminBuildingInfo from "@/components/admin/AdminBuildingInfo.vue"

describe('AdminBuildingInfo.vue', () => {

  let wrapper;

  beforeEach(() => {
    AdminBuildingInfo.beforeMount = () => Promise.resolve();
    wrapper = mount(AdminBuildingInfo);
  })

  it('render of component', () => {
    expect(wrapper.exists()).toBeTruthy();
  })

});
