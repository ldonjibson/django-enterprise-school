from .import views
from django.urls import path

urlpatterns = [
	path('', views.home, name="home_page"),
	path('students/', views.students_view, name="students_list"),
	path('students/<int:id>/', views.students_list_view, name="students_list_view"),
	path('students/add/', views.add_student, name="add_student"),
	path('students/del<int:id>/', views.delete_student, name="delete_student"),
	path('parents/', views.parents_view, name="parents_list"),
	path('parents/add/', views.add_parent, name="add_parent"),
	path('teachers/', views.teachers_view, name="teachers_list"),
	path('teachers/add/', views.add_teacher, name="add_teacher"),
	path('class/', views.class_view, name="class_list"),
	path('class/add/', views.add_class, name="add_class"),
	path('subject/', views.subjects_view, name="subjects_list"),
	path('subject/add/', views.add_subject, name="add_subject"),
	path('assign-teacher/', views.assign_teacher_view, name="assign_teacher_list"),
	path('assign-teacher/add/', views.add_assign_teacher, name="add_assign_teacher"),
	path('assign-section/', views.assign_section_view, name="assign_section_list"),
	path('assign-section/add/', views.add_assign_section, name="add_assign_section"),
	path('section/', views.section_view, name="sections_list"),
	path('section/add/', views.add_section, name="add_section"),
	path('attendance/', views.attendance_list, name="attendance_list"),
	path('attendance/add/', views.add_attendance, name="add_attendance"),
	path('score_entry/', views.score_list, name="score_list"),
	path('score_entry/add/', views.score_entry, name="score_entry"),
	path('api/chart/', views.expenditure_graph, name="expense_graph_url"),
	]