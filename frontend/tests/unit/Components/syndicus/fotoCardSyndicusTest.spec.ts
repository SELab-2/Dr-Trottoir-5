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
    const dataSyndicus = {time: new Date(), remark: "test Description", image: "test"}
    await wrapper.setProps({data: dataSyndicus})
    await wrapper.vm.$nextTick();
    const description = wrapper.find('[data-test="description"]');
    const image = wrapper.find('[data-test="image"]');
    const time = wrapper.find('[data-test="time"]');
    expect(description.text()).toMatch(dataSyndicus.remark)
    expect(image.attributes().src).toMatch(dataSyndicus.image)
    expect(time.text()).toMatch(dataSyndicus.time.toString())
  })

})
