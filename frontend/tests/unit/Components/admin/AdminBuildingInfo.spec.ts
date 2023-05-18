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
    AdminBuildingInfo.methods.open_manual = jest.fn();
    AdminBuildingInfo.methods.goEditPage = jest.fn();
    AdminBuildingInfo.methods.cancel_save = jest.fn();
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

  it('check for manual button and been pressed', async () => {
    const manualButton = wrapper.find('[data-test="manual-button"]')
    expect(manualButton.exists()).toBeTruthy();
    expect(wrapper.find('v-file-input ').exists()).toBeFalsy();
    await manualButton.trigger('click');
    expect(AdminBuildingInfo.methods.open_manual).toHaveBeenCalled();
  })

  it('check for afvalcontainer add', () => {
    expect(wrapper.find('[data-test="afval-button"]').exists()).toBeTruthy();
  })

  it('should not have edit button', () => {
    expect(wrapper.find('[data-test="save-button"]').exists()).toBeFalsy();
  })

  it('check for edit mode', async () => {
    await wrapper.setProps({edit: true});
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="afval-button"]').exists()).toBeFalsy();
    expect(wrapper.find('[data-test="save-button"]').exists()).toBeTruthy();
  })

  it('check for confirmdialog', () => {
    expect(wrapper.find('[data-test="dialog"]').exists()).toBeTruthy()
  })

  it('test if go to edit page works', async () => {
    await wrapper.vm.$nextTick();
    const editButton = wrapper.find('[data-test="edit-button"]');
    expect(editButton.exists()).toBeTruthy();
    await editButton.trigger('click');
    expect(AdminBuildingInfo.methods.goEditPage).toHaveBeenCalled();
  })

  it('cancel edit', async () => {
    await wrapper.setProps({edit: true});
    await wrapper.vm.$nextTick();
    const editButton = wrapper.find('[data-test="cancel-button"]');
    expect(editButton.exists()).toBeTruthy();
    await editButton.trigger('click');
    expect(AdminBuildingInfo.methods.cancel_save).toHaveBeenCalled();
  })

});
