import ltspice
import matplotlib.pyplot as plt
filepath = 'AGNI_SPICE_new\AGNI_SPICE_new\AGNI_SPICE\128b_no_A_to_B.raw'
l = ltspice.Ltspice(filepath)
l.parse() # Data loading sequence. It may take few minutes for huge file.

time = l.get_time()
# V1 = l.get_data('V(ns1_vcap)')
# plt.plot(time, V1)
# plt.show()
for i in range(l.case_count): # Iteration in simulation cases 
    time = l.get_time(i)
    # Case number starts from zero
    # Each case has different time point numbers
    V_cap = l.get_data('V(ns1_vcap)',i)
    plt.plot(time, V_cap)

plt.show()
# print(V1)