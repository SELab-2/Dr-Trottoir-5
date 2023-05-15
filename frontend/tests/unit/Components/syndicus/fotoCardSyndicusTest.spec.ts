import {mount} from "@vue/test-utils";
import FotoCardSyndicus from "@/components/syndicus/FotoCardSyndicus.vue";


describe("FotoCardSyndicus.vue", () => {

  let wrapper;
  beforeEach(() => {
    wrapper = mount(FotoCardSyndicus);
  })

  it("renders the component", () => {
    expect(wrapper.exists()).toBe(true);
  })

  it("renders the important information", () => {
    expect(wrapper.find('v-card')).toBeTruthy()
    expect(wrapper.find('v-card-text')).toBeTruthy()
  })

  it("renders the props data", async () => {
    const dataSyndicus = {timeStamp: new Date(), description: "test Description", imageURL: "test"}
    await wrapper.setProps({data: dataSyndicus})
    await wrapper.vm.$nextTick();
    const description = wrapper.find('[data-test="description"]');
    const image = wrapper.find('[data-test="image"]');
    const time = wrapper.find('[data-test="time"]');
    expect(description.text()).toMatch(dataSyndicus.description)
    expect(image.attributes().src).toMatch(dataSyndicus.imageURL)
    expect(time.text()).toMatch(dataSyndicus.timeStamp.toString())
  })

})
