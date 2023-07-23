datatime_now=`date "+%Y-%m-%d %H:%M"`
git config --global user.name "pavlov"
git config --global user.email "pavlov.web@mail.ru"
git add *
git commit -m "$datatime_now"
git branch -M main
git remote add origin https://github.com/Pavlov18/django_traning_website.git
git push -u origin main
