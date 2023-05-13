import {mount} from '@vue/test-utils'
import CreateEditPostStudent from "@/components/student/CreateEditPostStudent.vue";
import {triggerInput} from "../../../utils/testHelper";
import OverviewScreenStudentPosts from "@/components/student/OverviewScreenStudentPosts.vue";

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

describe('OverviewScreenStudentPost.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(OverviewScreenStudentPosts)
  })

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  })

  it('check building name', async () => {
    await wrapper.setProps({
      data: {buildingName: 'test', type: 'test', images: [], info: '', planning: '', building_id: ''}
    })

    expect(wrapper.find('h1').text()).toBe('test')
  })

  it('check type', async () => {
    await wrapper.setProps({
      data: {buildingName: 'test', type: 'test2', images: [], info: '', planning: '', building_id: ''}
    })

    expect(wrapper.find('h4').text()).toBe('test2')
  })

  it('goToPhotoPage is called when clicked on the icon', async () => {
    OverviewScreenStudentPosts.methods.goToPhotoPage = jest.fn()
    const wrapper = mount(OverviewScreenStudentPosts)
    const icon = wrapper.find('[data-test="goToFotoPage-button"]');
    await icon.trigger('click')
    await wrapper.vm.$nextTick();
    expect(OverviewScreenStudentPosts.methods.goToPhotoPage).toHaveBeenCalled()
  })

  it('completeTask is called when clicked on the icon', async () => {
    OverviewScreenStudentPosts.methods.completeTask = jest.fn()
    const wrapper = mount(OverviewScreenStudentPosts)
    const icon = wrapper.find('[data-test="completeTask-button"]');
    await icon.trigger('click')
    await wrapper.vm.$nextTick();
    expect(OverviewScreenStudentPosts.methods.completeTask).toHaveBeenCalled()
  })

})
