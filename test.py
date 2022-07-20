import model

proj2 = model.Project("Proj2", "Some random ramblings", "JJ")

allrecords = model.Project.select_all()