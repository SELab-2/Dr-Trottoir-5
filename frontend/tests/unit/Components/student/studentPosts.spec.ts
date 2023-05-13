import {mount} from '@vue/test-utils'
import CreateEditPostStudent from "@/components/student/CreateEditPostStudent.vue";
import {triggerInput} from "../../../utils/testHelper";

describe('CreateEditPostStudent.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(CreateEditPostStudent)
  })

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('Render "Klik om een foto toe te voegen"', () => {
    expect(wrapper.find('p').text()).toMatch('Klik om een foto toe te voegen')
  });

  it('remove image is called when the remove button is clicked and deleted the image', async () => {
    await wrapper.setData({imageUrl: 'test'})
    await wrapper.vm.$nextTick();
    const removeButton = wrapper.find('[data-test="delete-button"]');
    await removeButton.trigger('click')
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.imageUrl).toBe("")
  })

  it('call selectImage when clicked in the square', async () => {
    CreateEditPostStudent.methods.selectImage = jest.fn()
    const wrapper = mount(CreateEditPostStudent)
    const square = wrapper.find('[data-test="square-button"]');
    await square.trigger('click')
    await wrapper.vm.$nextTick();
    expect(CreateEditPostStudent.methods.selectImage).toHaveBeenCalled()
  })

  it('call uploadData when clicked on the upload button', async () => {
    CreateEditPostStudent.methods.uploadData = jest.fn()
    const wrapper = mount(CreateEditPostStudent)
    const uploadButton = wrapper.find('[data-test="upload-button"]');
    await uploadButton.trigger('click')
    await wrapper.vm.$nextTick();
    expect(CreateEditPostStudent.methods.uploadData).toHaveBeenCalled()
  })

  it('call editData when clicked on the edit button', async () => {
    CreateEditPostStudent.methods.editData = jest.fn()
    const wrapper = mount(CreateEditPostStudent)
    await wrapper.setProps({data: {edit: true}})
    await wrapper.vm.$nextTick();
    const editButton = wrapper.find('[data-test="edit-button"]');
    await editButton.trigger('click')
    await wrapper.vm.$nextTick();
    expect(CreateEditPostStudent.methods.editData).toHaveBeenCalled()
  })

  it('image check', async () => {
    await wrapper.setData({imageUrl: 'test'})
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.imageCheck).toBeTruthy()
  })

  it('set description', async () => {
    const description = wrapper.find('[data-test="description"]');
    description.element.value = 'test';
    const activator = (x) => {
      return {description: x}
    }
    triggerInput(description, wrapper, activator)
    expect(wrapper.vm.description).toBe('test')
  })

  /*it('show building name and type', async () => {
    const data = {nameBuilding: 'test', type: 'test', info: '', edit: false, id: '', planning: '', building_id: ''}
    await wrapper.setProps({data: {nameBuilding: 'test', type: 'test', info: '', edit: false, id: '', planning: '', building_id: ''}})
    wrapper.vm.$forceUpdate()
    const buildingName = wrapper.findComponent('[data-test="buildingName"]')
    const buildingType = wrapper.find('[data-test="buildingType"]')

    expect(buildingName.text()).toBe(data.nameBuilding)
    expect(buildingType.text()).toBe(data.type)
  })*/
})
