C:\Users\alumno\Desktop\Tarde_BigData\BigData_e_IA\BigData\05_Practica_Docker>docker create --name test1 debian tail -f dev/null
3d5a7eed0d53fe40a38dc706f028e4feb15570f8b6dba3d37364bd26d5a28fdc

C:\Users\alumno\Desktop\Tarde_BigData\BigData_e_IA\BigData\05_Practica_Docker>docker start test1
test1

C:\Users\alumno\Desktop\Tarde_BigData\BigData_e_IA\BigData\05_Practica_Docker>docker exec -it test1 /bin/bash
root@3d5a7eed0d53:/#
