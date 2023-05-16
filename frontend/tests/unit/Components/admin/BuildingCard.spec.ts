import {mount} from "@vue/test-utils";
import BuildingCard from "@/components/admin/BuildingCard.vue";

describe('BuildingCard.vue', () => {

  let wrapper

  const data = {
    name: 'Test Gebouw',
    id: 1,
    adres: 'TestStraat 1',
    ivago_klantnr: 1,
    buildingID: "test",
    manual: 1,
  }
  beforeEach(async () => {
    BuildingCard.beforeMount = () => Promise.resolve();
    wrapper = mount(BuildingCard, {
      props: data
    });
  });

  it('render of component', async () => {
    expect(wrapper.exists()).toBeTruthy();
  })

})
