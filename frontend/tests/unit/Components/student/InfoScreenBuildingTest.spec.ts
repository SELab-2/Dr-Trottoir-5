import { mount } from "@vue/test-utils";
import InfoScreenBuilding from "@/components/student/InfoScreenBuilding.vue";

describe("InfoScreenBuilding.vue", () => {

  let wrapper;

  beforeEach(() => {
    InfoScreenBuilding.created = jest.fn()
    wrapper = mount(InfoScreenBuilding);
  })

  it("renders the component", () => {
    expect(wrapper.exists()).toBe(true);
  })

  it("call downloadFile methode when clicked on the download button", async () => {
    InfoScreenBuilding.methods.downloadFile = jest.fn()
    const wrapper = mount(InfoScreenBuilding)
    const downloadButton = wrapper.find('[data-test="download-button"]');
    await downloadButton.trigger('click')
    await wrapper.vm.$nextTick();
    expect(InfoScreenBuilding.methods.downloadFile).toHaveBeenCalled()
  })

  it("render name building", async () => {
    await wrapper.setData({building: {name: 'test'}})
    const headerName = wrapper.find('[data-test="buildingName"]')
    expect(headerName.text()).toBe('test')
  })

  it("render text", async () => {
    const p = wrapper.find('p')
    const opmerking = wrapper.find('h2')
    expect(p.text()).toBe('Handleiding')
    expect(opmerking.text()).toBe('Opmerkingen:')
  })


  it('renders remarks correct', async () => {
    const remarks = ['Remark 1', 'Remark 2', 'Remark 3']

    await wrapper.setData({building: {remarks: remarks}})
    wrapper.vm.$nextTick();
    wrapper.vm.$forceUpdate()

    const remarkItems = wrapper.findAll('[data-test="remarks"]');
    expect(remarkItems).toHaveLength(remarks.length);

    remarkItems.forEach((item, index) => {
      expect(item.text()).toBe(remarks[index]);
    });
  });

})
