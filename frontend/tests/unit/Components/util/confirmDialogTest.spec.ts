import {mount} from '@vue/test-utils'
import ConfirmDialog from "@/components/util/ConfirmDialog.vue";

describe('ConfirmDialog.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(ConfirmDialog);
  })

  it('render', () => {
    expect(wrapper.exists()).toBe(true);
  })

  it('check that it renders the props', async () => {
    const confirmFunctionMock = jest.fn();

    await wrapper.setProps(
      {
        text: 'test',
        confirm_function: confirmFunctionMock
      }
    )

    const text = wrapper.find('p')
    expect(text.text()).toBe('test')
    const confirmButton = wrapper.find('[data-test="confirm_button"]')
    expect(confirmButton.text()).toBe('Ja')

    wrapper.vm.open();

    confirmButton.trigger('click')

    expect(confirmFunctionMock).toHaveBeenCalled();
  })

  it('check that dialog is closed', async () => {
    wrapper.setData({dialog: true})

    const closeButton = wrapper.find('[data-test="close_button"]')

    closeButton.trigger('click')

    expect(closeButton.text()).toBe('Nee')

    expect(wrapper.vm.dialog).toBe(false)
  })

  it('check important components', () => {
    expect(wrapper.find('v-dialog')).toBeTruthy()
    expect(wrapper.find('v-card')).toBeTruthy()
  })


})
