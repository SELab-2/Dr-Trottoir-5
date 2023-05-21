import { mount } from "@vue/test-utils";
import FotoCardStudent from "@/components/student/FotoCardStudent.vue";

describe("InfoScreenBuilding.vue", () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(FotoCardStudent);
  })

  it("renders the component", () => {
    expect(wrapper.exists()).toBe(true);
  })

  it("goToEditPage is called when clicked on the edit button", async () => {
    FotoCardStudent.methods.goToEditPage = jest.fn()
    wrapper = mount(FotoCardStudent)
    const editButton = wrapper.find('[data-test="edit-button"]');
    await editButton.trigger('click')
    await wrapper.vm.$nextTick();
    expect(FotoCardStudent.methods.goToEditPage).toHaveBeenCalled()
  })

  it("deletPost is called when clicked on the delete button", async () => {
    FotoCardStudent.methods.deletePost = jest.fn()
    wrapper = mount(FotoCardStudent)
    const deleteButton = wrapper.find('[data-test="delete-button"]');
    await deleteButton.trigger('click')
    await wrapper.vm.$nextTick();
    expect(FotoCardStudent.methods.deletePost).toHaveBeenCalled()
  })

  it("renders the important information", () => {
    expect(wrapper.find('v-card')).toBeTruthy()
    expect(wrapper.find('v-card-text')).toBeTruthy()
    expect(wrapper.find('[data-test="edit-button"]')).toBeTruthy()
    expect(wrapper.find('[data-test="delete-button"]')).toBeTruthy()
  })

  it("renders the props data", async () => {
    const data = {time: new Date(), remark: "testRemark", image: "test",id: 1}
    await wrapper.setProps({data: data})
    await wrapper.vm.$nextTick();
    const remark = wrapper.find('[data-test="remark"]');
    const image = wrapper.find('[data-test="image"]');
    const time = wrapper.find('[data-test="time"]');
    expect(remark.text()).toMatch(data.remark)
    expect(image.attributes().src).toMatch(data.image)
    expect(time.text()).toMatch(data.time.toLocaleString())
  })


})
