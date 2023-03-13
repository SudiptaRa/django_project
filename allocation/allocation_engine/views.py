from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# from rest_framework import viewsets
from allocation_engine.models import Employee_table
from allocation_engine.serializers import employeeSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from allocation_engine import controller






# Create your views here.

def Testing(request):
    return HttpResponse("Testing page")

# class employeeviewset(viewsets.ModelViewSet):
#     queryset = Employee_table.objects.all()
#     serializer_class = employeeSerializer

class Employeeviewset(ViewSet):

    def create(self,request):
        if ('id' not in request.data or not request.data['id']) or ('empid' not in request.data or not request.data['empid']):
            return Response({"error": False, "message": "id and empid required ", "status": 400}, status=status.HTTP_400_BAD_REQUEST)   
        cont_obj=controller.Controller()
        create_res = cont_obj.create_employee_details(request)
        if 'error' not in create_res:
            print(create_res)
            return Response({"error": False, "message": create_res['message'], "status": 200}, status=status.HTTP_200_OK)
        else:
            return Response({"error": True, "message": create_res['message'], "status": 400}, status=status.HTTP_400_BAD_REQUEST)




    # def update(self,request):
    #         new_data={}
    #         employee_data={}
    #         employee_data_set = Employee_table.objects.get(empid = request.data['empid'])
    #         if request.data:
    #             new_data['id'] = request.data['id']
    #             new_data['empid'] = request.data['empid']
    #             new_data['empname'] = request.data['empname']
    #             new_data['empemail'] = request.data['empemail']
    #             new_data['emppassword'] = request.data['emppassword']   
    #             new_data['empexp'] = request.data['empexp']      
    #             employee_data = employeeSerializer(employee_data_set, data=new_data)
    #             if employee_data.is_valid():
    #                 obj = employee_data.save()
    #             return Response({"error": False, "message": "success", "status": 200}, status=status.HTTP_200_OK)
    #         else:
    #             return Response({"error": False, "message": "failed", "status": 400}, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------------------------------------------------------------------------

    def update(self,request):
        update_res={}
        if 'id' not in request.data:
            return Response({"error": False, "message": "please provide id to update records", "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        employee_data_set = Employee_table.objects.get(id = request.data['id'])
        updt_obj = controller.Controller()
        update_res = updt_obj.update_employee_details(request)
        employee_data = employeeSerializer(employee_data_set,data=update_res,partial=True)
        if employee_data.is_valid():
            obj = employee_data.save()
        if 'error' not in update_res:
            return Response({"error": False, "message": "success", "status": 200}, status=status.HTTP_200_OK)
        else:
            return Response({"error": False, "message": update_res["message"], "status": 400}, status=status.HTTP_400_BAD_REQUEST)




    def delete(self,request,id):
        try:
            if id:
                member = Employee_table.objects.get(id = id)
                member.delete()
                return Response({"error": False, "message": "success", "status": 200}, status=status.HTTP_200_OK)
            else:
                return Response({"error": False, "message": "failed", "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
                return Response({"error": False, "message": f"we would like to inform you {ex}", "status": 400}, status=status.HTTP_400_BAD_REQUEST)

    def retrivingAll(self,request):
        try:
            employee_data={}
            if not request.data:
                employee_data = Employee_table.objects.all().values()            
                return Response({"error": False, "message": "success", "status": 200,"Data":employee_data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": False, "message": "failed", "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
                return Response({"error": False, "message": "failed", "status": 400}, status=status.HTTP_400_BAD_REQUEST)


    def retriv(self,request):
        try:
            employee_data={}

            if request.data:
                employee_data = Employee_table.objects.filter(id=request.data['id']).values() 
                return Response({"error": False, "message": "success", "status": 200,"Data":employee_data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": False, "message": "Please provide the empid", "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
                return Response({"error": False, "message": ex.args, "status": 400}, status=status.HTTP_400_BAD_REQUEST)


