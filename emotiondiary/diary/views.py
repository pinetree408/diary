from django.views.generic import TemplateView

class DiaryView(TemplateView):
	template_name = "diary/diary.html"
