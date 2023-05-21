import {mount} from "@vue/test-utils"
import NormalButton from "@/components/NormalButton.vue"

describe('NormalButton.vue', () => {

  let wrapper;

  const data = {
    text: 'TestButton',
    dropDown: false,
    parentFunction: jest.fn()
  }

  beforeEach(() => {
    wrapper = mount(NormalButton, {
      propsData: data
    })
  })

  it('render of component', () => {
    expect(wrapper.exists).toBeTruthy();
  })

  it('text is present', () => {
    const button = wrapper.find('v-btn');
    expect(button.text()).toBe('TestButton');
  })

  it('click button', async () => {
    const button = wrapper.find('v-btn');
    await button.trigger('click');
    expect(wrapper.vm.$props.parentFunction).toHaveBeenCalled();
  })

})
