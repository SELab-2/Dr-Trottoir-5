import {mount} from '@vue/test-utils';
import AccountInformation from "@/components/AccountInformation.vue"
import NormalButton from "@/components/NormalButton.vue";
import ConfirmDialog from "@/components/util/ConfirmDialog.vue"

describe('AccountInformation.vue', () => {

  const dataOfComponent = {
    first_name: 'Test',
    last_name: 'Tester',
    email: 'test@test.com',
    phone_nr: '0474441313',
    role: 'ST',
  }

  let wrapper;

  beforeEach(async () => {
    AccountInformation.props.get_data = {
      type: Function, default: () => {
        return dataOfComponent
      }
    };
    wrapper = await mount(AccountInformation);
  })


  it('render the comonent', () => {
    expect(wrapper.exists()).toBeTruthy();
  })

  it('user data is shown without edit', async () => {
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.$data.data.first_name === dataOfComponent.first_name).toBeTruthy();
    expect(wrapper.vm.$data.data.last_name === dataOfComponent.last_name).toBeTruthy();
    expect(wrapper.vm.$data.data.email === dataOfComponent.email).toBeTruthy();
    expect(wrapper.vm.$data.data.phone_nr === dataOfComponent.phone_nr).toBeTruthy();
    expect(wrapper.vm.$data.data.role === dataOfComponent.role).toBeTruthy();
    expect(wrapper.find('v-btn').attributes('icon')).toBeFalsy();
  });

  it('user can be deleted by admin', async () => {
    await wrapper.setProps({not_admin: false, can_edit_permission: true});
    expect(wrapper.findComponent(NormalButton).text()).toBe('Pas aan');
    expect(wrapper.findComponent(ConfirmDialog).exists()).toBeTruthy();
    expect(wrapper.find('[data-test="delete-button"]').exists()).toBeTruthy();
  });

  it('user can not be deleted by admin', async () => {
    await wrapper.setProps({not_admin: true, can_edit_permission: true});
    expect(wrapper.findComponent(NormalButton).text()).toBe('Pas aan');
    expect(wrapper.find('[data-test="delete-button"]').exists()).toBeFalsy();
  });

  it('user can not edit data', async () => {
    const wrapper = await mount(AccountInformation);
    await wrapper.setProps({not_admin: true, can_edit_permission: false})
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="edit-button"]').exists()).toBeFalsy()
    expect(wrapper.find('[data-test="save-button"]').exists()).toBeFalsy();
    expect(wrapper.find('[data-test="cancel-button"]').exists()).toBeFalsy();
  })

  it('user can edit data', async () => {
    await wrapper.setProps({not_admin: true, can_edit_permission: true})
    const editButton = wrapper.find('[data-test="edit-button"]')
    expect(editButton.exists()).toBeTruthy()
    await editButton.trigger('click');
    expect(wrapper.find('[data-test="save-button"]').exists()).toBeTruthy();
    expect(wrapper.find('[data-test="cancel-button"]').exists()).toBeTruthy();
  })
})
