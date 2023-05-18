import {mount} from "@vue/test-utils"
import AdminBuildingInfo from "@/components/admin/AdminBuildingInfo.vue"

describe('AdminBuildingInfo.vue', () => {

  let wrapper;

  const data = {
    name: 'Test gebouw',
    adres: 'Teststraat 1',
    locations: [],
    manual: {file: 'test.pdf', fileType: 'pdf', manualStatus: 'Klaar'},
    ivago_klantnr: 34,
    planningen: [],
    new_manual: null,
    selectedLocation: 1,
    errors: null
  }

  beforeEach(() => {
    AdminBuildingInfo.beforeMount = () => Promise.resolve();
    wrapper = mount(AdminBuildingInfo);
  })

  it('render of component', () => {
    expect(wrapper.exists()).toBeTruthy();
  });

  it('check if data is present', async () => {
    await wrapper.setData(data);
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="name"]').attributes().modelvalue).toBe('Test gebouw');
    expect(wrapper.find('[data-test="adres"]').attributes().modelvalue).toBe('Teststraat 1')
    expect(wrapper.find('[data-test="location"]').attributes().modelvalue).toBe("1");
    expect(wrapper.find('[data-test="client-nr"]').attributes().modelvalue).toBe("34");
  });

});
