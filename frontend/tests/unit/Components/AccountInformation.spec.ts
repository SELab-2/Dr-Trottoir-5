import {mount} from '@vue/test-utils';
import AccountInformation from "@/components/AccountInformation.vue"

describe('AccountInformation.vue', () => {

  const dataOfComponent = {
    data: {
      first_name: 'Test',
      last_name: 'Tester',
      email: 'test@test.com',
      phone_nr: '0474441313',
      role: 'ST',
    }
  }

  it('render the comonent', () => {
    const wrapper = mount(AccountInformation);
    expect(wrapper.exists()).toBeTruthy();
  })

  it('user data is shown', async () => {
    const wrapper = mount(AccountInformation);
    await wrapper.setData(dataOfComponent);
    await wrapper.vm.$nextTick();
    const inputs = wrapper.findAll('v-text-field').map(field => field.text());
    expect(inputs.includes(dataOfComponent.data.first_name)).toBeTruthy();
    expect(inputs.includes(dataOfComponent.data.last_name)).toBeTruthy();
    expect(inputs.includes(dataOfComponent.data.email)).toBeTruthy();
    expect(inputs.includes(dataOfComponent.data.phone_nr)).toBeTruthy();
    expect(inputs.includes(dataOfComponent.data.role)).toBeTruthy();
  });

})
