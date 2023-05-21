import {mount} from "@vue/test-utils"
import AdminBuildingInfoEdit from "@/components/admin/AdminBuildingInfoEdit.vue"

describe('AdminBuildingInfoEdit.vue', () => {

  let wrapper;

  const data = {
    name: 'Test gebouw',
    adres: 'Teststraat 1',
    manual: {file: 'test.pdf', fileType: 'pdf', manualStatus: 'Klaar'},
    ivago_klantnr: 34,
    planningen: [],
    new_manual: null,
    errors: null
  }

  beforeEach(() => {
    AdminBuildingInfoEdit.beforeMount = () => Promise.resolve();
    AdminBuildingInfoEdit.methods.save = jest.fn();
    AdminBuildingInfoEdit.methods.cancel_save = jest.fn();
    wrapper = mount(AdminBuildingInfoEdit);
  })

  it('render of component', () => {
    expect(wrapper.exists()).toBeTruthy();
  });

  it('check if data is present', async () => {
    await wrapper.setData(data);
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="name"]').attributes('model-value')).toBe('Test gebouw');
    expect(wrapper.find('[data-test="adres"]').attributes('model-value')).toBe('Teststraat 1')
    expect(wrapper.find('[data-test="client-nr"]').attributes('model-value')).toBe("34");
    expect(wrapper.find('[data-test="manual"]').exists()).toBeTruthy();
  });

  it('should have save and cancel button', () => {
    expect(wrapper.find('[data-test="save-button"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="cancel-button"]').exists()).toBeTruthy();
  })

  it('check for confirmdialog', () => {
    expect(wrapper.find('[data-test="dialog"]').exists()).toBeTruthy()
  })

  it('test save', async () => {
    const saveButton = wrapper.find('[data-test="save-button"]');
    expect(saveButton.exists()).toBeTruthy();
    await saveButton.trigger('click');
    expect(AdminBuildingInfoEdit.methods.save).toHaveBeenCalled();
  })

  it('cancel edit', async () => {
    await wrapper.setProps({edit: true});
    await wrapper.vm.$nextTick();
    const editButton = wrapper.find('[data-test="cancel-button"]');
    expect(editButton.exists()).toBeTruthy();
    await editButton.trigger('click');
    expect(AdminBuildingInfoEdit.methods.cancel_save).toHaveBeenCalled();
  })

});
