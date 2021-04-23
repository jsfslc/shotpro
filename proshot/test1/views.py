from django.shortcuts import render
from .forms import QuestionForm, subsetForm
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from .models import Question, test, Choice, Feedback, Answered, subset
import json, random
from django.core import serializers
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist
import traceback
from django.views.generic import TemplateView


def index(request):
    return render(request, "testAdmin/base.html")

class listviewIndex(ListView):
    print('en el index')
    model = Question
    template_name = "testAdmin/base.html"
    context_object_name = 'questions'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['subset'] = subset.objects.all()
        context['test'] = test.objects.get(pk=1)
        context['answers'] = Choice.objects.all()
        context['validarTest'] = validarTest()
        return context

#subset 
class Addsubset(CreateView):
    print('en el Addsubset')
    model = subset
    form_class = subsetForm
    template_name = "testAdmin/CRUD/subset/addSubset.html"    
    success_url = reverse_lazy('test1:index')

class EditSubset(UpdateView):    
    model= subset
    form_class = subsetForm
    template_name = "testAdmin/CRUD/subset/editSubset.html"    
    success_url = reverse_lazy('test1:index')

class deleteSubset(DeleteView):
    model= subset
    template_name = "testAdmin/CRUD/subset/deleteSubset.html"
    success_url = reverse_lazy('test1:index')


#questions
class addQuestion(TemplateView):
    template_name= 'testAdmin/CRUD/question/addQuestion.html'
    success_url = reverse_lazy('test1:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formQuestion"] =  QuestionForm()

        return context

    def post(self, request, *args, **kwargs):
        data ={}
        try:
            print('request.post ',request.POST)
            formQuestion = QuestionForm(request.POST, request.FILES or None)
            if formQuestion.is_valid():
                questionText = formQuestion.cleaned_data['question_text']
                questionUrl = formQuestion.cleaned_data['question_url']
                questionImage = formQuestion.cleaned_data['question_imagen']
                score = formQuestion.cleaned_data['subset']
                newquestion = Question(question_text= questionText, question_url=questionUrl, question_imagen=questionImage, score= score,test=test.objects.get(pk=1))
                newquestion.save()
                # aqui falta guardar las respuestas para la pregunta
                """ antes usaba el AJAX para agregar las respuestas, me funcionmaba bien pero al momento 
                de editar las respuestas asociadas a todo, me iba a la B
                    radios = json.loads(request.POST.get('radios'))
                    print(type(radios))
                    print(radios)
                    for elements in radios:
                        print(elements[1])
                        addAnswers = Choice(question = newquestion,  choice_text=elements[1] , is_valid = elements[2] )
                        addAnswers.save()
                    ser_newquestion = serializers.serialize('json', [ newquestion, ])
                    return JsonResponse({ 'newquestion': ser_newquestion}, status=200)

                """

                                              
                return HttpResponseRedirect(reverse_lazy('test1:index'))
            return render(request, 'testAdmin/CRUD/question/addQuestion.html', {'formQuestion': formQuestion})
        except Exception as e:
            data['error'] = str(e)
        
class editQuestion(UpdateView):

    model = Question
    form_class = QuestionForm
    template_name = 'testAdmin/CRUD/question/editQuestion.html'
    success_url = reverse_lazy('test1:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.all() 
        return context 

class deleteQuestion(DeleteView):
    model= Question
    template_name = "testAdmin/CRUD/question/deleteQuestion.html"
    success_url = reverse_lazy('test1:index')



#Questionario
def showQuestions(request,test_id):
    try: 
        TEST = test.objects.get(pk = test_id)
    except(KeyError, TEST.DoesNotExist):
        raise Http404
    else:    
        new_test = Feedback()
        new_test.totalscore = 0 
        new_test.user = request.user
        new_test.save()   
        #new_test.user.add(request.user)
        #new_test.user.add(User.objects.get(id=1))
        request.session['ID_TEST'] = new_test.id
        lista = []

        i = 0
        while i < 1: #se tiene que colocar la cantidad de preguntas que se quiere obtener
            #ne este caso sería una por categoría
            for subsets in subset.objects.all():              
                questions = Question.objects.values_list('id', flat=True).filter(score=subsets).order_by('?').first()
                print(f"se saco la siguiente pregunta random {questions}")
                #for elements in questions:
                while questions in lista:
                    print(f" la pregunta ya esta en la lista {questions}")
                    questions = Question.objects.values_list('id', flat=True).filter(score=subsets).order_by('?').first()
                lista.append(questions)
                new_answered =  Answered(feedback= new_test, question=Question.objects.get(pk=questions))
                new_answered.save()
            i+=1

            #questions = Question.objects.values_list(id, flat=True).order_by('?')[:2]
            #questions.values_list(id, flat=True)
            #lista.append(questions)
           
            #for question in Question.objects.filter(score = subsets):
                #print(question.order_by('?')[:1])
                #print(type(question))

        #questions = Question.objects.all()
    
        """      
        for element in lista:
            print(element)
            new_answered =  Answered(feedback= new_test, question=Question.objects.get(pk=element))
            new_answered.save()

        """    
        #for preguntas in Answered.objects.filter(feedback=new_test):
        #    print( " preguntas.question " , preguntas.question)
            
        #asdf = Question.objects.filter(pk=lista)
        #print("asdf",asdf)
        
        
        print(Answered.objects.filter(feedback=new_test))
        #print('filtrado de preguntas', Question.objects.filter(id= lista))
        testin = Answered.objects.filter(feedback=new_test)
        #print(Answered__question.values())
        answers = Choice.objects.all()
        #questions = Question.objects.order_by('?')[:4]
        #MyModel.objects.order_by('?')[:2]
        questions = Question.objects.all()

        context = {
            'test': TEST,
            'questions' : questions,
            'answers'   : answers,
            'lista' : lista,
            'new_answered' : Answered.objects.filter(feedback=new_test),
            #'last_question' : Question.objects.last(),
        }
        
        return render(request ,'testAdmin/test.html',context )



    
def saveAnswers(request):
    try:
        #owner = User.objects.get(pk=1)
        answer_id = request.session['ID_TEST']
        this_answer = Feedback.objects.get(pk=answer_id)        
    except (KeyError, Feedback.DoesNotExist):
        raise Http404
    else:       
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            totalscore = 0
            #----depurar
            #------------
            try:        
                for i in range(Question.objects.first().id , Question.objects.last().id + 1 ):
                    try:
                        choiced = Choice.objects.get(pk=request.POST.get("radio_"+ str(i)))
                    except ObjectDoesNotExist:
                        continue
                    else:
                        if choiced.is_valid is True:
                            print(Question.objects.get(pk=i))
                            print('la espuesta es true')
                            print(Question.objects.get(pk=i).score.value)
                            totalscore += Question.objects.get(pk=i).score.value    
                        elif choiced is None:
                            print(Question.objects.get(pk=i))
                            print('la respuesta es falsa')
                            continue
                        else:
                            continue
                        #guardar respuesta
                        respondido = Answered(question = Question.objects.get(pk=i), choice = Choice.objects.get(pk=request.POST.get("radio_"+ str(i))), feedback = this_answer)
                        respondido.save()
                this_answer.totalscore = totalscore
                this_answer.save()
                #this_answer.status = 2
                #this_answer.save()
                return HttpResponseRedirect(reverse('test1:test_cert', args=(this_answer.id,)))
            except Exception as e:
                print (type(e))
                trace_back = traceback.format_exc()
                message = str(e)+ " " + str(trace_back)
                print (message)
                raise Http404
        else:
            raise Http404

def test_certificate(request,id):
        #return render(request, 'certificate/body_BARRAT_certificate.html', context)
        respuestas = Answered.objects.filter(feedback=id)
        resultado = Feedback.objects.get(pk=id)
        choices = Choice.objects.all()
        subconjuntos = subset.objects.all()
        prueba = test.objects.get(pk=1)
        contadorSubconjunto= []
        contadorSubconjunto2= []
        i =0
        """
        for grupo in subconjuntos:
            for respondido in respuestas:
                if respondido.choice.is_valid and respondido.question.score.pk == grupo.pk:
                    #contadorSubconjunto[grupo.pk] = +1 
                    print('subconjunto -> ', grupo.name_subset)
                    #contadorSubconjunto2(grupo.name_subset) = i
                    #i=+1
                    contadorSubconjunto.append(grupo.pk)
                else:
                    continue
        for grupo in subconjuntos:
            print(contadorSubconjunto.count(grupo.pk))
        """
        print(type(respuestas))
        context ={
            'respuestas': respuestas,
            'feedback' : resultado,
            'prueba' : prueba,
            'resultado' : choices,
            'subconjuntos' : subconjuntos,
            'contadorSubconjunto':contadorSubconjunto,

        }
        return render(request, 'testAdmin/testCertificate.html', context)


def rendirTest(request):
    prueba = test.objects.get(pk=1)
    questions = Question.objects.filter(test=prueba)
    context = {
        'test' : prueba,
        'questions' : questions,
        'validarTest' : validarTest(),
    }
    return render(request, "testAdmin/dartest.html",context)



def verResultados(request):
    return render(request, "testAdmin/resultados.html")

def validarTest():
    for subsets in subset.objects.all(): 
        if not Question.objects.filter(score=subsets):
            print('validartest Falso')
            return False
            break
    return True

class listFeedbackView(ListView):
    print('en el feedback')
    model = Feedback
    template_name = "testAdmin/resultados.html"
    context_object_name = 'feedback'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['test'] = test.objects.get(pk=1)        
        return context
