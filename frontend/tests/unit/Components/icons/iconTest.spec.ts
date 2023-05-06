import { mount } from '@vue/test-utils'
import DeleteIcon from '@/components/icons/DeleteIcon.vue'
import EditIcon from '@/components/icons/EditIcon.vue'
import InfoIcon from '@/components/icons/InfoIcon.vue'


describe('Test Icon components', () => {
  it('renders a delete icon with the correct color', () => {
    const wrapper = mount(DeleteIcon)
    const avatar = wrapper.find('.button-style')
    const icon = avatar.find('v-icon')

    expect(avatar.attributes('color')).toBe('#F0533D')
    expect(icon.text()).toBe('mdi-delete')
    expect(icon.attributes('color')).toBe('white')
  })

  it('renders a Edit icon with the correct color', () => {
    const wrapper = mount(EditIcon)
    const avatar = wrapper.find('.button-style')
    const icon = avatar.find('v-icon')

    expect(avatar.attributes('color')).toBe('#FFE600')
    expect(icon.text()).toBe('mdi-pencil')
    expect(icon.attributes('color')).toBe('white')
  })

  it('renders a Edit icon with the correct color', () => {
    const wrapper = mount(InfoIcon)
    const avatar = wrapper.find('.button-style')
    const icon = avatar.find('v-icon')

    expect(avatar.attributes('color')).toBe('#9DCF62')
    expect(icon.text()).toBe('mdi-information-variant')
    expect(icon.attributes('color')).toBe('white')
  })
})

