import pandapower as pp
import math

def overhead_network(power):
    net = pp.create_empty_network()

    # LV Overhead 100mm
    pp.create_std_type(net, {"r_ohm_per_km": 0.270922,
                             "x_ohm_per_km": (0.06416027 * 10 ** -3) * math.pi * 50,
                             "c_nf_per_km": 0,
                             "max_i_ka": 0.271,
                             "type": "ol",
                             "temperature_degree_celsius": 20,

                             }, name="LV Overhead 100mm Al", element="line"
                       )
    # LV Overhead 50mm
    pp.create_std_type(net, {"r_ohm_per_km": 0.5419,
                             "x_ohm_per_km": (0.06416027 * 10 ** -3) * math.pi * 50,
                             "c_nf_per_km": 0,
                             "max_i_ka": 0.181,
                             "type": "ol",
                             "temperature_degree_celsius": 20,
                             }, name="LV Overhead 50mm Al", element="line"
                       )

    # LV Overhead 14mm
    pp.create_std_type(net, {"r_ohm_per_km": 1.273,
                             "x_ohm_per_km": 0,
                             "c_nf_per_km": 0,
                             "max_i_ka": 0.099,
                             "r0_ohm_per_km": 1.273,
                             "x0_ohm_per_km": 0,
                             "c0_nf_per_km": 0,
                             "type": "ol",
                             "temperature_degree_celsius": 20,
                             }, name="LV Overhead 14mm", element="line"
                       )

    # Substation buses
    SubstationMVbus = pp.create_bus(net, vn_kv=11, name="SubMV_Terminal", in_service=True)
    SubstationLVbus = pp.create_bus(net, vn_kv=0.4, name="SubLV_Terminal", in_service=True)

    # External Grid
    ExternalGrid = pp.create_ext_grid(net, bus=SubstationMVbus, vm_pu=1)

    # Transformer
    Transformer = pp.create_transformer_from_parameters(net, hv_bus=SubstationMVbus, lv_bus=SubstationLVbus,
                                                        name="Dyn11",
                                                        sn_mva=0.63, vn_hv_kv=11, vn_lv_kv=0.400,
                                                        vkr_percent=0.8571429, vk_percent=4, pfe_kw=5.4, i0_percent=0,
                                                        vk0_percent=3, vkr0_percent=0, shift_degree=330, tap_side="hv",
                                                        tap_step_percent=2.5, tap_neutral=3, tap_min=1, tap_max=5,
                                                        tap_pos=3, mag0_rx=4.558264, mag0_percent=1.51942,
                                                        vector_group="Dyn", )

    # Medium buses
    bus1 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus1", in_service=True)
    bus2 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus2", in_service=True)
    bus3 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus3", in_service=True)
    bus4 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus4", in_service=True)
    bus5 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus5", in_service=True)
    bus6 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus6", in_service=True)
    bus7 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus7", in_service=True)
    bus8 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus8", in_service=True)

    # Medium Lines
    LineM1 = pp.create_line(net, from_bus=SubstationLVbus, to_bus=bus1, length_km=0.100,
                            std_type="LV Overhead 100mm Al",
                            name="LineM1", in_service=True)
    #LineM1_B = pp.create_line(net, from_bus=SubstationLVbus, to_bus=bus1, length_km=0.100,
       #                       std_type="LV Overhead 100mm Al",
        #                      name="LineM1_B", in_service=True)
    LineM2 = pp.create_line(net, from_bus=bus1, to_bus=bus2, length_km=0.05, std_type="LV Overhead 100mm Al",
                            name="LineM2",
                            in_service=True)
    #LineM2_B = pp.create_line(net, from_bus=bus1, to_bus=bus2, length_km=0.05, std_type="LV Overhead 100mm Al",
     #                         name="LineM2_B",
      #                        in_service=True)
    LineM3 = pp.create_line(net, from_bus=bus2, to_bus=bus3, length_km=0.025, std_type="LV Overhead 100mm Al",
                            name="LineM3", in_service=True)
    #LineM3_B = pp.create_line(net, from_bus=bus2, to_bus=bus3, length_km=0.025, std_type="LV Overhead 100mm Al",
     #                         name="LineM3_B", in_service=True)
    LineM4 = pp.create_line(net, from_bus=bus3, to_bus=bus4, length_km=0.025, std_type="LV Overhead 100mm Al",
                            name="LineM4", in_service=True)
    #LineM4_B = pp.create_line(net, from_bus=bus3, to_bus=bus4, length_km=0.025, std_type="LV Overhead 100mm Al",
     #                         name="LineM4_B", in_service=True)
    LineM5 = pp.create_line(net, from_bus=bus4, to_bus=bus5, length_km=0.100, std_type="LV Overhead 100mm Al",
                            name="LineM5", in_service=True)
    LineM6 = pp.create_line(net, from_bus=bus5, to_bus=bus6, length_km=0.050, std_type="LV Overhead 100mm Al",
                            name="LineM6", in_service=True)
    LineM7 = pp.create_line(net, from_bus=bus6, to_bus=bus7, length_km=0.025, std_type="LV Overhead 100mm Al",
                            name="LineM7", in_service=True)
    LineM8 = pp.create_line(net, from_bus=bus7, to_bus=bus8, length_km=0.025, std_type="LV Overhead 100mm Al",
                            name="LineM8", in_service=True)

    """     Buses, lines and loads from BUS1    """
    # buses
    bus11 = pp.create_bus(net, vn_kv=0.4, name="bus11", in_service=True)
    bus11_1 = pp.create_bus(net, vn_kv=0.4, name="bus111", in_service=True)
    bus11_2 = pp.create_bus(net, vn_kv=0.4, name="bus112", in_service=True)
    bus112 = pp.create_bus(net, vn_kv=0.4, name="bus12", in_service=True)
    bus112_1 = pp.create_bus(net, vn_kv=0.4, name="bus121", in_service=True)
    bus112_2 = pp.create_bus(net, vn_kv=0.4, name="bus122", in_service=True)

    # Lines
    lineT11 = pp.create_line(net, from_bus=bus1, to_bus=bus11, name="lineT11", length_km=0.035,
                             std_type="LV Overhead 50mm Al", in_service=True)
    lineT12 = pp.create_line(net, from_bus=bus11, to_bus=bus112, name="lineT12", length_km=0.035,
                             std_type="LV Overhead 50mm Al", in_service=True)
    lineP1 = pp.create_line(net, from_bus=bus11, to_bus=bus11_1, name="lineP1", length_km=0.020,
                            std_type="LV Overhead 14mm", in_service=True)
    lineP2 = pp.create_line(net, from_bus=bus11, to_bus=bus11_2, name="lineP2", length_km=0.020,
                            std_type="LV Overhead 14mm", in_service=True)
    lineP3 = pp.create_line(net, from_bus=bus112, to_bus=bus112_1, name="lineP3", length_km=0.020,
                            std_type="LV Overhead 14mm", in_service=True)
    lineP4 = pp.create_line(net, from_bus=bus112, to_bus=bus112_2, name="lineP4", length_km=0.020,
                            std_type="LV Overhead 14mm", in_service=True)

    # Loads
    # load26 = pp.create_load_from_cosphi(net, bus=bus11_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load25 = pp.create_load_from_cosphi(net, bus=bus11_2, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load24 = pp.create_load_from_cosphi(net, bus=bus112_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load21 = pp.create_load_from_cosphi(net, bus=bus112_2, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS2    """
    bus21 = pp.create_bus(net, vn_kv=0.4, name="bus21", in_service=True)
    bus22 = pp.create_bus(net, vn_kv=0.4, name="bus22", in_service=True)

    lineP5 = pp.create_line(net, from_bus=bus2, to_bus=bus21, name="lineP5", length_km=0.020,
                            std_type="LV Overhead 14mm",
                            in_service=True)
    lineP6 = pp.create_line(net, from_bus=bus2, to_bus=bus22, name="lineP6", length_km=0.020,
                            std_type="LV Overhead 14mm",
                            in_service=True)
    #
    # load2 = pp.create_load_from_cosphi(net, bus=bus21, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load3 = pp.create_load_from_cosphi(net, bus=bus22, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS3    """
    bus31 = pp.create_bus(net, vn_kv=0.4, name="bus31", in_service=True)
    bus32 = pp.create_bus(net, vn_kv=0.4, name="bus32", in_service=True)

    lineP7 = pp.create_line(net, from_bus=bus3, to_bus=bus31, length_km=0.020, name="lineP7",
                            std_type="LV Overhead 14mm",
                            in_service=True)
    lineP8 = pp.create_line(net, from_bus=bus3, to_bus=bus32, length_km=0.020, name="lineP8",
                            std_type="LV Overhead 14mm",
                            in_service=True)

    # load27 = pp.create_load_from_cosphi(net, bus=bus31, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load4 = pp.create_load_from_cosphi(net, bus=bus32, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS4    """
    bus42 = pp.create_bus(net, vn_kv=0.4, name="bus42", in_service=True)
    bus41 = pp.create_bus(net, vn_kv=0.4, name="bus41", in_service=True)
    bus412 = pp.create_bus(net, vn_kv=0.4, name="bus412", in_service=True)
    bus41_2 = pp.create_bus(net, vn_kv=0.4, name="bus41_2", in_service=True)
    bus41_1 = pp.create_bus(net, vn_kv=0.4, name="bus41_1", in_service=True)

    lineP10 = pp.create_line(net, from_bus=bus4, to_bus=bus42, name="lineP10", length_km=0.020,
                             std_type="LV Overhead 14mm",
                             in_service=True)
    lineT21 = pp.create_line(net, from_bus=bus4, to_bus=bus41, name="lineT21", length_km=0.035,
                             std_type="LV Overhead 50mm Al", in_service=True)
    lineT22 = pp.create_line(net, from_bus=bus41, to_bus=bus412, name="lineT22", length_km=0.035,
                             std_type="LV Overhead 50mm Al", in_service=True)
    lineP11 = pp.create_line(net, from_bus=bus41, to_bus=bus41_1, name="lineP11", length_km=0.020,
                             std_type="LV Overhead 14mm", in_service=True)
    lineP12 = pp.create_line(net, from_bus=bus41, to_bus=bus41_2, name="lineP12", length_km=0.020,
                             std_type="LV Overhead 14mm", in_service=True)

    # Loads
    # load5 = pp.create_load_from_cosphi(net, bus=bus42, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load10 = pp.create_load_from_cosphi(net, bus=bus41_2, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load11 = pp.create_load_from_cosphi(net, bus=bus41_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load22 = pp.create_load_from_cosphi(net, bus=bus412, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load23 = pp.create_load_from_cosphi(net, bus=bus412, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS5    """
    # buses
    bus52 = pp.create_bus(net, vn_kv=0.4, name="bus53", in_service=True)
    bus51 = pp.create_bus(net, vn_kv=0.4, name="bus51", in_service=True)
    bus512 = pp.create_bus(net, vn_kv=0.4, name="bus512", in_service=True)

    bus51_1 = pp.create_bus(net, vn_kv=0.4, name="bus51_1", in_service=True)
    bus51_2 = pp.create_bus(net, vn_kv=0.4, name="bus51_2", in_service=True)
    bus512_1 = pp.create_bus(net, vn_kv=0.4, name="bus52_1", in_service=True)
    bus512_2 = pp.create_bus(net, vn_kv=0.4, name="bus52_2", in_service=True)

    # lines
    lineT31 = pp.create_line(net, from_bus=bus5, to_bus=bus51, name="lineT31", length_km=0.035,
                             std_type="LV Overhead 100mm Al", in_service=True)
    lineT32 = pp.create_line(net, from_bus=bus51, to_bus=bus512, name="lineT32", length_km=0.035,
                             std_type="LV Overhead 50mm Al", in_service=True)

    lineP15 = pp.create_line(net, from_bus=bus5, to_bus=bus52, name="lineP15", length_km=0.020,
                             std_type="LV Overhead 14mm",
                             in_service=True)
    lineP16 = pp.create_line(net, from_bus=bus51, to_bus=bus51_1, name="lineP16", length_km=0.020,
                             std_type="LV Overhead 14mm", in_service=True)
    lineP17 = pp.create_line(net, from_bus=bus51, to_bus=bus51_2, name="lineP17", length_km=0.020,
                             std_type="LV Overhead 14mm", in_service=True)
    lineP18 = pp.create_line(net, from_bus=bus512, to_bus=bus512_1, name="lineP18", length_km=0.020,
                             std_type="LV Overhead 14mm", in_service=True)
    lineP19 = pp.create_line(net, from_bus=bus512, to_bus=bus512_2, name="lineP19", length_km=0.020,
                             std_type="LV Overhead 14mm", in_service=True)

    # Loads
    # load9 = pp.create_load_from_cosphi(net, bus=bus52, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load13 = pp.create_load_from_cosphi(net, bus=bus51_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load14 = pp.create_load_from_cosphi(net, bus=bus51_2, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load12 = pp.create_load_from_cosphi(net, bus=bus512_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load6 = pp.create_load_from_cosphi(net, bus=bus512_2, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS6    """
    # buses
    bus61 = pp.create_bus(net, vn_kv=0.4, name="bus61", in_service=True)
    bus62 = pp.create_bus(net, vn_kv=0.4, name="bus62", in_service=True)

    # lines
    lineP20 = pp.create_line(net, from_bus=bus6, to_bus=bus61, name="lineP20", length_km=0.020,
                             std_type="LV Overhead 14mm",
                             in_service=True)
    lineP21 = pp.create_line(net, from_bus=bus6, to_bus=bus62, name="lineP21", length_km=0.020,
                             std_type="LV Overhead 14mm",
                             in_service=True)

    # Loads
    # load7 = pp.create_load_from_cosphi(net, bus=bus62, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load8 = pp.create_load_from_cosphi(net, bus=bus61, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS7    """
    bus71 = pp.create_bus(net, vn_kv=0.4, name="bus71", in_service=True)
    lineP22 = pp.create_line(net, from_bus=bus7, to_bus=bus71, name="lineP22", length_km=0.020,
                             std_type="LV Overhead 14mm",
                             in_service=True)
    # load1 = pp.create_load_from_cosphi(net, bus=bus71, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS8    """
    # buses
    bus81 = pp.create_bus(net, vn_kv=0.4, name="bus81", in_service=True)
    bus82 = pp.create_bus(net, vn_kv=0.4, name="bus82", in_service=True)
    bus83 = pp.create_bus(net, vn_kv=0.4, name="bus83", in_service=True)
    bus834 = pp.create_bus(net, vn_kv=0.4, name="bus834", in_service=True)
    bus83_1 = pp.create_bus(net, vn_kv=0.4, name="bus83_1", in_service=True)
    bus83_2 = pp.create_bus(net, vn_kv=0.4, name="bus83_2", in_service=True)

    # lines
    lineP23 = pp.create_line(net, from_bus=bus8, to_bus=bus81, name="lineP23", length_km=0.020,
                             std_type="LV Overhead 14mm",
                             in_service=True)
    lineP24 = pp.create_line(net, from_bus=bus8, to_bus=bus82, name="lineP24", length_km=0.020,
                             std_type="LV Overhead 14mm",
                             in_service=True)
    lineP25 = pp.create_line(net, from_bus=bus83, to_bus=bus83_1, name="lineP25", length_km=0.020,
                             std_type="LV Overhead 14mm", in_service=True)
    lineP26 = pp.create_line(net, from_bus=bus83, to_bus=bus83_2, name="lineP26", length_km=0.020,
                             std_type="LV Overhead 14mm", in_service=True)
    lineT41 = pp.create_line(net, from_bus=bus8, to_bus=bus83, name="lineT41", length_km=0.035,
                             std_type="LV Overhead 50mm Al", in_service=True)
    lineT42 = pp.create_line(net, from_bus=bus83, to_bus=bus834, name="lineT42", length_km=0.035,
                             std_type="LV Overhead 50mm Al", in_service=True)

    # loads
    # load15 = pp.create_load_from_cosphi(net, bus=bus81, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load16 = pp.create_load_from_cosphi(net, bus=bus82, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load19 = pp.create_load_from_cosphi(net, bus=bus83_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load20 = pp.create_load_from_cosphi(net, bus=bus83_2, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load17 = pp.create_load_from_cosphi(net, bus=bus834, sn_mva=0.002, cos_phi=0.85, mode="ind")
    # load18 = pp.create_load_from_cosphi(net, bus=bus834, sn_mva=0.002, cos_phi=0.85, mode="ind")

    list_of_loadbuses = [11, 12, 14, 15, 16, 17, 18, 19, 20, 23, 24, 22, 22, 25, 28, 29, 30, 31, 33, 32, 34, 35, 36, 39,
                         40, 38, 38]

    for loadbus in list_of_loadbuses:
        pp.create_load_from_cosphi(net, bus=loadbus, sn_mva=power, cos_phi=0.85, mode="ind")

    return net








