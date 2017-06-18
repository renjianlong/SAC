import obspy as ob
st = ob.read('SC.XJI.2008131160002.D.00.BHN.sac')
print(st)
print(st[0].stats)
print(st[0].data)
print(len(st[0].data))
st.plot()
st.write('', format='SAC')