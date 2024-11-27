import turtle

# יצירת חלון עבור הציור
window = turtle.Screen()
window.title("Turtle")

# יצירת מטורף (turtle)
pen = turtle.Turtle()

# הגדרת מהירות ורוחב קו
pen.speed(1) # מהירות 1 מהירות הכי איטית
pen.pensize(3) # רוחב קו 3 פיקסלים

# ציור ריבוע
for _ in range(4):
    pen.forward(100) # צעד קדימה באורך 100 פיקסלים
    pen.right(90) # סיבוב ימינה בזווית של 90 מעלות

# סגירת החלון בלחיצה עליו
window.mainloop()
