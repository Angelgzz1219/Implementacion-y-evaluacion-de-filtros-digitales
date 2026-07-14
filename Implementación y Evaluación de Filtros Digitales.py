Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
... plt.plot(t, senal_pba)
... plt.title('Filtro pasa bandas')
...
... plt.tight_layout()
... plt.show()
...
... # ------------------------------------------
... # Respuestas en frecuencia
... # ------------------------------------------
...
... plt.figure(figsize=(12,6))
...
... plt.plot((fs*0.5/np.pi)*w_pb,
...          20*np.log10(abs(h_pb)),
...          label='Pasa bajos')
...
... plt.plot((fs*0.5/np.pi)*w_pa,
...          20*np.log10(abs(h_pa)),
...          label='Pasa altos')
...
... plt.plot((fs*0.5/np.pi)*w_pba,
...          20*np.log10(abs(h_pba)),
...          label='Pasa bandas')
...
... plt.title('Respuesta en frecuencia')
... plt.xlabel('Frecuencia (Hz)')
... plt.ylabel('Magnitud (dB)')
... plt.grid()
... plt.legend()
... plt.show()
