import { mount } from "@vue/test-utils";
import DayPlanBuilding from "@/components/student/DayPlanBuilding.vue";

describe("dayPlanBuilding.vue", () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(DayPlanBuilding);
  })

  it("renders", () => {
    expect(wrapper.exists()).toBe(true);
  });

  it("buildingClicked is called when clicked on the building", async () => {
    DayPlanBuilding.methods.buildingClicked = jest.fn()
    wrapper = mount(DayPlanBuilding)
    const building = wrapper.find('[data-test="building"]');
    await building.trigger('click')
    await wrapper.vm.$nextTick();
    expect(DayPlanBuilding.methods.buildingClicked).toHaveBeenCalled()
  })

  it("render important components", () => {
    expect(wrapper.find('v-card')).toBeTruthy()
    expect(wrapper.find('v-card-title')).toBeTruthy()
    expect(wrapper.find('[data-test="building"]')).toBeTruthy()
  })

  it("render status div", async () => {
    expect(wrapper.find('[data-test="status"]').text()).toBe("Status")
  })

  it("test colour unknown", async () => {
    const data = {building: {status: 'Onbekend'}}
    await wrapper.setProps({data: data})
    await wrapper.vm.$nextTick();
    const building = wrapper.find('[data-test="building"]');
    expect(building.attributes().color).toBe('red-lighten-1')
  })

  it("test colour succeeded", async () => {
    const data = {building: {status: 'Voltooid'}}
    await wrapper.setProps({data: data})
    await wrapper.vm.$nextTick();
    const building = wrapper.find('[data-test="building"]');
    expect(building.attributes().color).toBe('green-lighten-1')
  })

  it("test colour still running", async () => {
    const data = {building: {status: 'Bezig'}}
    await wrapper.setProps({data: data})
    await wrapper.vm.$nextTick();
    const building = wrapper.find('[data-test="building"]');
    expect(building.attributes().color).toBe('yellow-lighten-1')
  })

  it("check building name", async () => {
    const data = {building: {name: 'test'}}
    await wrapper.setProps({data: data})
    const name = wrapper.find('[data-test="name-building"]');
    expect(name.text()).toBe('test')
  })

  it("check building adres", async () => {
    const data = {building: {adres: 'test'}}
    await wrapper.setProps({data: data})
    const name = wrapper.find('[data-test="adres-building"]');
    expect(name.text()).toBe('test')
  })

  it("check building status", async () => {
    const data = {building: {status: 'test'}}
    await wrapper.setProps({data: data})
    const name = wrapper.find('[data-test="status-building"]');
    expect(name.text()).toBe('test')
  })

});
