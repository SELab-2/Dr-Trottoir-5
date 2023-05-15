import {mount} from "@vue/test-utils"
import LoginTopBar from "@/components/LoginTopBar.vue"

describe('LoginTopBar.vue', () => {

  it('render of component', () => {
    const wrapper = mount(LoginTopBar);
    expect(wrapper.exists()).toBeTruthy();
  });

  it('rendering of v-app-bar', async () => {
    // Mount doesn't render templates
    const wrapper = mount(LoginTopBar);
    await wrapper.vm.$nextTick();
    const appBar = wrapper.find('v-app-bar');
    expect(appBar.exists()).toBeTruthy();
  });


})
