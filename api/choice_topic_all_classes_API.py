from flask import render_template, redirect, request
import flask
from forms.mainpageForm import LogMainPageForm
from data import db_session
from data.users import Info, TrainerStatistics
from flask_login import current_user

blueprint = flask.Blueprint(
    'choicetopicallclasses_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/<int:num_class>', methods=['GET', 'POST'])
def choice_topic_all_classes_trainer(num_class):
    profile = LogMainPageForm()

    page = f'choice_topic_all_classes_trainer,{num_class}'

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.user_id == current_user.id).first()
    user_name = current_user.name
    user_surname = current_user.surname
    user_email = current_user.email
    user_avatar = f"../{user_info.avatar_href}"

    if request.method == 'POST':
        time_spent = request.form.get('time')
        correct_answers = request.form.get('correct_answers', type=int)
        total_questions = request.form.get('total_questions', type=int)
        topic = request.form.get('topic')

        print(f"Time spent: {time_spent}")
        print(f"Correct answers: {correct_answers}")
        print(f"Total questions: {total_questions}")
        print(f"Topic: {topic}")
        trainer_statistic = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                    num_class == TrainerStatistics.num_class,
                                                                    topic == TrainerStatistics.topic).first()

        time = int(time_spent.split(":")[0]) + round(int(time_spent.split(":")[1]) / 60, 1)

        if trainer_statistic.full_time is None:
            trainer_statistic.full_time = time
        else:
            trainer_statistic.full_time += time

        if trainer_statistic.total_questions is None:
            trainer_statistic.total_questions = total_questions
        else:
            trainer_statistic.total_questions += total_questions

        if trainer_statistic.correct_questions is None:
            trainer_statistic.correct_questions = correct_answers
        else:
            trainer_statistic.correct_questions += correct_answers

        db_sess.commit()

        trainer_statistic.accuracy = str(round(trainer_statistic.correct_questions / trainer_statistic.total_questions,
                                               2) * 100)

        trainer_statistic.speed = str(
            round(trainer_statistic.correct_questions / trainer_statistic.full_time, 2))

        db_sess.commit()

    all_accuracies = []
    all_speeds = []
    all_times = []

    trainer_statistic11 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Счет предметов").first()
    trainer_statistic12 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Многоугольники").first()
    trainer_statistic13 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Задачки на увеличение").first()
    trainer_statistic14 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Задачки на уменьшение").first()
    trainer_statistic15 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Задачки (разнобой)").first()
    trainer_statistic16 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Примеры на счет").first()

    trainer_statistic21 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Числа от 1 до 20").first()
    trainer_statistic22 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Счет десятками").first()
    trainer_statistic23 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Сложение и вычитание (Числа от 1 до 100)").first()
    trainer_statistic24 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Уравнения").first()
    trainer_statistic25 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Деление и умножение (Начальные)").first()
    trainer_statistic26 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Примеры").first()

    trainer_statistic31 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Сложение (Трехзначные числа)").first()
    trainer_statistic32 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Вычитание (Трехзначные числа)").first()
    trainer_statistic33 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Деление (Среднее)").first()
    trainer_statistic34 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Умножение (Среднее)").first()
    trainer_statistic35 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Деление (Трехзначные числа)").first()
    trainer_statistic36 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Примеры (Трехзначные числа)").first()

    trainer_statistic41 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Сложение (Три слагаемых)").first()
    trainer_statistic42 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Сложение (Числа больше 1000)").first()
    trainer_statistic43 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Умножение (На произведение)").first()
    trainer_statistic44 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Умножение (Продвинутое)").first()
    trainer_statistic45 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Деление (На двузначные)").first()
    trainer_statistic46 = db_sess.query(TrainerStatistics).filter(current_user.id == TrainerStatistics.user_id,
                                                                  num_class == TrainerStatistics.num_class,
                                                                  TrainerStatistics.topic == "Деление (Продвинутое)").first()
    if num_class == 1:
        if not (trainer_statistic11.full_time is None):
            accuracy = trainer_statistic11.accuracy
            speed = trainer_statistic11.speed
            full_time = trainer_statistic11.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic12.full_time is None):
            accuracy = trainer_statistic12.accuracy
            speed = trainer_statistic12.speed
            full_time = trainer_statistic12.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic13.full_time is None):
            accuracy = trainer_statistic13.accuracy
            speed = trainer_statistic13.speed
            full_time = trainer_statistic13.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic14.full_time is None):
            accuracy = trainer_statistic14.accuracy
            speed = trainer_statistic14.speed
            full_time = trainer_statistic14.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic15.full_time is None):
            accuracy = trainer_statistic15.accuracy
            speed = trainer_statistic15.speed
            full_time = trainer_statistic15.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic16.full_time is None):
            accuracy = trainer_statistic16.accuracy
            speed = trainer_statistic16.speed
            full_time = trainer_statistic16.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))

    if num_class == 2:
        if not (trainer_statistic21.full_time is None):
            accuracy = trainer_statistic21.accuracy
            speed = trainer_statistic21.speed
            full_time = trainer_statistic21.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic22.full_time is None):
            accuracy = trainer_statistic22.accuracy
            speed = trainer_statistic22.speed
            full_time = trainer_statistic22.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic23.full_time is None):
            accuracy = trainer_statistic23.accuracy
            speed = trainer_statistic23.speed
            full_time = trainer_statistic23.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic24.full_time is None):
            accuracy = trainer_statistic24.accuracy
            speed = trainer_statistic24.speed
            full_time = trainer_statistic24.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic25.full_time is None):
            accuracy = trainer_statistic25.accuracy
            speed = trainer_statistic25.speed
            full_time = trainer_statistic25.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic26.full_time is None):
            accuracy = trainer_statistic26.accuracy
            speed = trainer_statistic26.speed
            full_time = trainer_statistic26.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))

    elif num_class == 3:
        if not (trainer_statistic31.full_time is None):
            accuracy = trainer_statistic31.accuracy
            speed = trainer_statistic31.speed
            full_time = trainer_statistic31.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic32.full_time is None):
            accuracy = trainer_statistic32.accuracy
            speed = trainer_statistic32.speed
            full_time = trainer_statistic32.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic33.full_time is None):
            accuracy = trainer_statistic33.accuracy
            speed = trainer_statistic33.speed
            full_time = trainer_statistic33.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic34.full_time is None):
            accuracy = trainer_statistic34.accuracy
            speed = trainer_statistic34.speed
            full_time = trainer_statistic34.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic35.full_time is None):
            accuracy = trainer_statistic35.accuracy
            speed = trainer_statistic35.speed
            full_time = trainer_statistic35.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic36.full_time is None):
            accuracy = trainer_statistic36.accuracy
            speed = trainer_statistic36.speed
            full_time = trainer_statistic36.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))

    elif num_class == 4:
        if not (trainer_statistic41.full_time is None):
            accuracy = trainer_statistic41.accuracy
            speed = trainer_statistic41.speed
            full_time = trainer_statistic41.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic42.full_time is None):
            accuracy = trainer_statistic42.accuracy
            speed = trainer_statistic42.speed
            full_time = trainer_statistic42.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic43.full_time is None):
            accuracy = trainer_statistic43.accuracy
            speed = trainer_statistic43.speed
            full_time = trainer_statistic43.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic44.full_time is None):
            accuracy = trainer_statistic44.accuracy
            speed = trainer_statistic44.speed
            full_time = trainer_statistic44.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic45.full_time is None):
            accuracy = trainer_statistic45.accuracy
            speed = trainer_statistic45.speed
            full_time = trainer_statistic45.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))
        if not (trainer_statistic46.full_time is None):
            accuracy = trainer_statistic46.accuracy
            speed = trainer_statistic46.speed
            full_time = trainer_statistic46.full_time
        else:
            accuracy = "0.00"
            speed = "0.00"
            full_time = "0:00"
        all_accuracies.append(accuracy)
        all_speeds.append(speed)
        all_times.append(str(full_time))

    colors = ["purple", "indigo", "green", "teal", "light-purple", "red-orange"]
    back_colors = ["#CE93D8", "#9FA8DA", "#b3ffcc", "#80CBC4", "#D1C4E9", "#FFAB91"]

    topics = {1: {
        "Счет предметов": {"Ваша точность:": all_accuracies[0],
                           "Ваша скорость ответов:": all_speeds[0],
                           "Общее время:": all_times[0]},
        "Многоугольники": {"Ваша точность:": all_accuracies[1],
                           "Ваша скорость ответов:": all_speeds[1],
                           "Общее время:": all_times[1]},
        "Задачки на увеличение": {"Ваша точность:": all_accuracies[2],
                                  "Ваша скорость ответов:": all_speeds[2],
                                  "Общее время:": all_times[2]},
        "Задачки на уменьшение": {"Ваша точность:": all_accuracies[3],
                                  "Ваша скорость ответов:": all_speeds[3],
                                  "Общее время:": all_times[3]},
        "Задачки (разнобой)": {"Ваша точность:": all_accuracies[4],
                               "Ваша скорость ответов:": all_speeds[4],
                               "Общее время:": all_times[4]},
        "Примеры на счет": {"Ваша точность:": all_accuracies[5],
                            "Ваша скорость ответов:": all_speeds[5],
                            "Общее время:": all_times[5]}
    },
        2: {
            "Числа от 1 до 20": {"Ваша точность:": all_accuracies[0],
                                 "Ваша скорость ответов:": all_speeds[0],
                                 "Общее время:": all_times[0]},
            "Счет десятками": {"Ваша точность:": all_accuracies[1],
                               "Ваша скорость ответов:": all_speeds[1],
                               "Общее время:": all_times[1]},
            "Сложение и вычитание (Числа от 1 до 100)": {"Ваша точность:": all_accuracies[2],
                                                         "Ваша скорость ответов:": all_speeds[2],
                                                         "Общее время:": all_times[2]},
            "Уравнения": {"Ваша точность:": all_accuracies[3],
                          "Ваша скорость ответов:": all_speeds[3],
                          "Общее время:": all_times[3]},
            "Деление и умножение (Начальные)": {"Ваша точность:": all_accuracies[4],
                                                "Ваша скорость ответов:": all_speeds[4],
                                                "Общее время:": all_times[4]},
            "Примеры": {"Ваша точность:": all_accuracies[5],
                        "Ваша скорость ответов:": all_speeds[5],
                        "Общее время:": all_times[5]}
        },
        3: {
            "Сложение (Трехзначные числа)": {"Ваша точность:": all_accuracies[0],
                                             "Ваша скорость ответов:": all_speeds[0],
                                             "Общее время:": all_times[0]},
            "Вычитание (Трехзначные числа)": {"Ваша точность:": all_accuracies[1],
                                              "Ваша скорость ответов:": all_speeds[1],
                                              "Общее время:": all_times[1]},
            "Деление (Среднее)": {"Ваша точность:": all_accuracies[2],
                                  "Ваша скорость ответов:": all_speeds[2],
                                  "Общее время:": all_times[2]},
            "Умножение (Среднее)": {"Ваша точность:": all_accuracies[3],
                                    "Ваша скорость ответов:": all_speeds[3],
                                    "Общее время:": all_times[3]},
            "Деление (Трехзначные числа)": {"Ваша точность:": all_accuracies[4],
                                            "Ваша скорость ответов:": all_speeds[4],
                                            "Общее время:": all_times[4]},
            "Примеры (Трехзначные числа)": {"Ваша точность:": all_accuracies[5],
                                            "Ваша скорость ответов:": all_speeds[5],
                                            "Общее время:": all_times[5]}
        },
        4: {
            "Сложение (Три слагаемых)": {"Ваша точность:": all_accuracies[0],
                                         "Ваша скорость ответов:": all_speeds[0],
                                         "Общее время:": all_times[0]},
            "Сложение (Числа больше 1000)": {"Ваша точность:": all_accuracies[1],
                                             "Ваша скорость ответов:": all_speeds[1],
                                             "Общее время:": all_times[1]},
            "Умножение (На произведение)": {"Ваша точность:": all_accuracies[2],
                                            "Ваша скорость ответов:": all_speeds[2],
                                            "Общее время:": all_times[2]},
            "Умножение (Продвинутое)": {"Ваша точность:": all_accuracies[3],
                                        "Ваша скорость ответов:": all_speeds[3],
                                        "Общее время:": all_times[3]},
            "Деление (На двузначные)": {"Ваша точность:": all_accuracies[4],
                                        "Ваша скорость ответов:": all_speeds[4],
                                        "Общее время:": all_times[4]},
            "Деление (Продвинутое)": {"Ваша точность:": all_accuracies[5],
                                      "Ваша скорость ответов:": all_speeds[5],
                                      "Общее время:": all_times[5]}
        }}

    if profile.settings.data:
        return redirect(f"/settings?next={page}")

    if profile.change_avatar.data:
        return redirect(f"/change_avatar?next={page}")

    if profile.exit.data:
        return redirect(f"/logout")

    return render_template("choice_topic.html", num_class=num_class, profile=profile,
                           avatar=user_avatar, name=user_name, surname=user_surname,
                           email=user_email, topics=topics, colors=colors, back_colors=back_colors)
