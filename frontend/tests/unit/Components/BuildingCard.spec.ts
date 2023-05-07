import {shallowMount} from "@vue/test-utils";
import BuildingCard from "@/components/admin/BuildingCard.vue";

describe('BuildingCard.vue', () => {

  it('render of component', () => {
    const wrapper = shallowMount(BuildingCard)
    expect(wrapper.exists()).toBeTruthy();
  })

})
