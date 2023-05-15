import {mount} from "@vue/test-utils"
import LoginTopBar from "@/components/LoginTopBar.vue"

describe('LoginTopBar.vue', () => {

  it('render of component', () => {
    const wrapper = mount(LoginTopBar);
    expect(wrapper.exists()).toBeTruthy();
  });

  it('button text login true', async () => {
    const wrapper = mount(LoginTopBar);
    await wrapper.vm.$nextTick();
    const button = wrapper.find('v-btn');
    expect(button.text()).toBe('Aanmelden');
  });


})
