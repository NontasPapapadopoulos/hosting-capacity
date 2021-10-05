import pandapower as pp
import math
from pandapower import plotting


def underground_network():
    net = pp.create_empty_network()

    # LV 300c AI 3,5-C
    pp.create_std_type(net, {"r_ohm_per_km": 0.0958,
                             "x_ohm_per_km": 0.07,
                             "c_nf_per_km": 330,        #0.33μF,330
                             "max_i_ka": 0.42,
                             "r0_ohm_per_km": 0.34838,
                             "x0_ohm_per_km": 1.2328,
                             "type": "cs",
                             "temperature_degree_celsius": 20,
                             }, name="LV 300c", element="line"
                       )

    #  LV 100mm AI OH Line
    pp.create_std_type(net, {"r_ohm_per_km": 0.270922,
                             "x_ohm_per_km": 0.257383,
                             "c_nf_per_km": 0,
                             "max_i_ka": 0.271,
                             "r0_ohm_per_km": 0.554544,
                             "x0_ohm_per_km": 1.030687,
                             "c0_nf_per_km": 0,
                             "type": "ol",
                             "temperature_degree_celsius": 20,
                             }, name="LV 100mm", element="line"
                       )


    # LV 22mm AI O/H Service
    pp.create_std_type(net, {"r_ohm_per_km": 1.227056,
                             "x_ohm_per_km": 0,
                             "c_nf_per_km": 0,
                             "max_i_ka": 0.155,
                             "r0_ohm_per_km": 1.227056,
                             "x0_ohm_per_km": 0,
                             "c0_nf_per_km": 0,
                             "type": "ol",
                             "temperature_degree_celsius": 20,
                             }, name="LV 22mm", element="line"
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
    bus1 = pp.create_bus(net, vn_kv=0.4, name="Med_bus1", in_service=True)
    bus2 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus2", in_service=True)
    bus3 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus3", in_service=True)
    bus4 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus4", in_service=True)
    bus5 = pp.create_bus(net, vn_kv=0.4, name="Med_Bus5", in_service=True)


    # Medium Lines
    LineM1 = pp.create_line(net, from_bus=SubstationLVbus, to_bus=bus1, length_km=0.100, std_type="LV 300c",
                            name="LineM1", in_service=True)
    LineM2 = pp.create_line(net, from_bus=bus1, to_bus=bus2, length_km=0.022, std_type="LV 300c", name="LineM2",
                            in_service=True)
    LineM3 = pp.create_line(net, from_bus=bus2, to_bus=bus3, length_km=0.077, std_type="LV 100mm",
                            name="LineM3", in_service=True)
    LineM4 = pp.create_line(net, from_bus=bus3, to_bus=bus4, length_km=0.070, std_type="LV 100mm",
                            name="LineM4", in_service=True)
    LineM5 = pp.create_line(net, from_bus=bus4, to_bus=bus5, length_km=0.030, std_type="LV 100mm",
                            name="LineM5", in_service=True)

    """     Buses, lines and loads from BUS1    """
    # buses
    bus11 = pp.create_bus(net, vn_kv=0.4, name="bus11", in_service=True)
    bus12 = pp.create_bus(net, vn_kv=0.4, name="bus12", in_service=True)
    bus13 = pp.create_bus(net, vn_kv=0.4, name="bus13", in_service=True)
    bus12_1 = pp.create_bus(net, vn_kv=0.4, name="bus12_1", in_service=True)
    bus12_2 = pp.create_bus(net, vn_kv=0.4, name="bus12_2", in_service=True)
    bus13_1 = pp.create_bus(net, vn_kv=0.4, name="bus13_1", in_service=True)
    bus13_2 = pp.create_bus(net, vn_kv=0.4, name="bus13_2", in_service=True)

    # lines from bus to bus
    Line11 = pp.create_line(net, from_bus=bus1, to_bus=bus11, length_km=0.014, name="Line11", std_type="LV 22mm", in_service=True)
    Line12 = pp.create_line(net, from_bus=bus1, to_bus=bus12, length_km=0.052, name="Line12", std_type="LV 100mm", in_service=True)
    Line123 = pp.create_line(net, from_bus=bus12, to_bus=bus13, length_km=0.052, name="Line23", std_type="LV 100mm", in_service=True)

    # lines from bus12 to loads
    Line12_1 = pp.create_line(net, from_bus=bus12, to_bus=bus12_1, length_km=0.014, name="Line2_1", std_type="LV 22mm", in_service=True)
    Line12_2 = pp.create_line(net, from_bus=bus12, to_bus=bus12_2, length_km=0.014, name="Line2_2", std_type="LV 22mm", in_service=True)

    # lines from bus13 to loads
    Line13_1 = pp.create_line(net, from_bus=bus13, to_bus=bus13_1, length_km=0.014, name="Line3_1", std_type="LV 22mm", in_service=True)
    Line13_2 = pp.create_line(net, from_bus=bus13, to_bus=bus13_2, length_km=0.014, name="Line3_2", std_type="LV 22mm", in_service=True)


    # loads
    Load11 = pp.create_load_from_cosphi(net, bus=bus11, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load121 = pp.create_load_from_cosphi(net, bus=bus12_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load122 = pp.create_load_from_cosphi(net, bus=bus12_2, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load131 = pp.create_load_from_cosphi(net, bus=bus13_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load132 = pp.create_load_from_cosphi(net, bus=bus13_2, sn_mva=0.002, cos_phi=0.85, mode="ind")

    Load132_ = pp.create_load_from_cosphi(net, bus=bus13_1, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS2    """
    # buses
    bus21 = pp.create_bus(net, vn_kv=0.4, name="bus21", in_service=True)
    bus22 = pp.create_bus(net, vn_kv=0.4, name="bus22", in_service=True)

    # lines
    Line21 = pp.create_line(net, from_bus=bus2, to_bus=bus21, length_km=0.014, std_type="LV 22mm", name="Line21", in_service=True)
    Line22 = pp.create_line(net, from_bus=bus2, to_bus=bus22, length_km=0.014, std_type="LV 22mm", name="Line22", in_service=True)

    # loads
    Load21 = pp.create_load_from_cosphi(net, bus=bus21, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load22 = pp.create_load_from_cosphi(net, bus=bus22, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS3    """
    # buses
    bus31 = pp.create_bus(net, vn_kv=0.4, name="bus31", in_service=True)
    bus32 = pp.create_bus(net, vn_kv=0.4, name="bus32", in_service=True)
    bus33 = pp.create_bus(net, vn_kv=0.4, name="bus33", in_service=True)

    bus32_1 = pp.create_bus(net, vn_kv=0.4, name="bus32_1", in_service=True)
    bus32_2 = pp.create_bus(net, vn_kv=0.4, name="bus32_2", in_service=True)

    bus33_1 = pp.create_bus(net, vn_kv=0.4, name="bus33_1", in_service=True)
    bus33_2 = pp.create_bus(net, vn_kv=0.4, name="bus33_2", in_service=True)

    # lines from bus to bus
    Line32 = pp.create_line(net, from_bus=bus3, to_bus=bus32, length_km=0.052, std_type="LV 100mm", name="Line32", in_service=True)
    Line323 = pp.create_line(net, from_bus=bus32, to_bus=bus33, length_km=0.052, std_type="LV 100mm", name="Line33", in_service=True)

    #lines from buses to loads
    Line31 = pp.create_line(net, from_bus=bus3, to_bus=bus31, length_km=0.014, std_type="LV 22mm", name="line31", in_service=True)

    Line32_1 = pp.create_line(net, from_bus=bus32, to_bus=bus32_1, length_km=0.014, std_type="LV 22mm", name="line32_1", in_service=True)
    Line32_2 = pp.create_line(net, from_bus=bus32, to_bus=bus32_2, length_km=0.014, std_type="LV 22mm", name="line32_2", in_service=True)

    Line33_1 = pp.create_line(net, from_bus=bus33, to_bus=bus33_1, length_km=0.014, std_type="LV 22mm", name="line33_1", in_service=True)
    Line33_2 = pp.create_line(net, from_bus=bus33, to_bus=bus33_2, length_km=0.014, std_type="LV 22mm", name="line33_2", in_service=True)

    #loads
    Load31 = pp.create_load_from_cosphi(net, bus=bus31, sn_mva=0.002, cos_phi=0.85, mode="ind")

    Load321 = pp.create_load_from_cosphi(net, bus=bus32_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load322 = pp.create_load_from_cosphi(net, bus=bus32_2, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load331 = pp.create_load_from_cosphi(net, bus=bus33_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load332 = pp.create_load_from_cosphi(net, bus=bus33_2, sn_mva=0.002, cos_phi=0.85, mode="ind")

    Load332_ = pp.create_load_from_cosphi(net, bus=bus33_2, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS4    """
    # buses
    bus41 = pp.create_bus(net, vn_kv=0.4, name="bus41", in_service=True)
    bus42 = pp.create_bus(net, vn_kv=0.4, name="bus42", in_service=True)

    # lines
    Line41 = pp.create_line(net, from_bus=bus4, to_bus=bus41, length_km=0.014, std_type="LV 22mm", name="Line41", in_service=True)
    Line42 = pp.create_line(net, from_bus=bus4, to_bus=bus42, length_km=0.014, std_type="LV 22mm", name="Line42", in_service=True)

    #loads
    Load41 = pp.create_load_from_cosphi(net, bus=bus41, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load42 = pp.create_load_from_cosphi(net, bus=bus42, sn_mva=0.002, cos_phi=0.85, mode="ind")

    """     Buses, lines and loads from BUS5    """
    #buses
    bus51 = pp.create_bus(net, vn_kv=0.4, name="bus51", in_service=True)
    bus52 = pp.create_bus(net, vn_kv=0.4, name="bus52", in_service=True)
    bus53 = pp.create_bus(net, vn_kv=0.4, name="bus53", in_service=True)

    bus52_1 = pp.create_bus(net, vn_kv=0.4, name="bus52_1", in_service=True)
    bus52_2 = pp.create_bus(net, vn_kv=0.4, name="bus52_2", in_service=True)
    bus53_1 = pp.create_bus(net, vn_kv=0.4, name="bus53_1", in_service=True)
    bus53_2 = pp.create_bus(net, vn_kv=0.4, name="bus53_2", in_service=True)

    #lines from bus to bus
    Line52 = pp.create_line(net, from_bus=bus5, to_bus=bus52, length_km=0.052, std_type="LV 100mm", name="Line52", in_service=True)
    Line523 = pp.create_line(net, from_bus=bus52, to_bus=bus53, length_km=0.052, std_type="LV 100mm", name="Line53", in_service=True)

    # lines from buses to loads
    Line51 = pp.create_line(net, from_bus=bus5, to_bus=bus51, length_km=0.014, std_type="LV 22mm", name="Line51", in_service=True)
    Line52_1 = pp.create_line(net, from_bus=bus52, to_bus=bus52_1, length_km=0.014, std_type="LV 22mm", name="Line52_1", in_service=True)
    Line52_2 = pp.create_line(net, from_bus=bus52, to_bus=bus52_2, length_km=0.014, std_type="LV 22mm", name="Line52_2", in_service=True)
    Line53_1 = pp.create_line(net, from_bus=bus53, to_bus=bus53_1, length_km=0.014, std_type="LV 22mm", name="Line53_1", in_service=True)
    Line53_2 = pp.create_line(net, from_bus=bus53, to_bus=bus53_2, length_km=0.014, std_type="LV 22mm", name="Line53_2", in_service=True)

    # loads
    Load51 = pp.create_load_from_cosphi(net, bus=bus51, sn_mva=0.002, cos_phi=0.85, mode="ind")

    Load521 = pp.create_load_from_cosphi(net, bus=bus52_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load522 = pp.create_load_from_cosphi(net, bus=bus52_2, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load531 = pp.create_load_from_cosphi(net, bus=bus53_1, sn_mva=0.002, cos_phi=0.85, mode="ind")
    Load532 = pp.create_load_from_cosphi(net, bus=bus53_2, sn_mva=0.002, cos_phi=0.85, mode="ind")

    Load532_ = pp.create_load_from_cosphi(net, bus=bus53_2, sn_mva=0.002, cos_phi=0.85, mode="ind")

    return net




