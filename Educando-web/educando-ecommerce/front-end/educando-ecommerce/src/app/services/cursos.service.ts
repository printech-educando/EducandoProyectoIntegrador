import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Curso } from '../interfaces/cursos.interface';
import { HttpClient } from '@angular/common/http';
import { Categoria } from '../interfaces/categoria.interface';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})

export class CursosService {

  // URL de la API para obtener cursos
  private apiUrl = environment.apiUrl;

  constructor(
    private http:HttpClient
  ) { }

  // Obtiene todos los cursos
  public getCursos(): Observable<Curso> {
    return this.http.get<Curso>(`${this.apiUrl}curso/`);
  }

  // Obtiene todas las categorías
  public getCategorias(): Observable<Categoria> {
    return this.http.get<Categoria>(`${this.apiUrl}categoria/`);
  }

  // Método para obtener un curso por su ID
  public obtenerCursoPorId(idCurso: number): Observable<Curso> {
    return this.http.get<Curso>(`${this.apiUrl}curso/${idCurso}/`);
  }

  // Obtiene los cursos por categoría
  public getCursosPorCategoria(idCategoria: number): Observable<Curso> {
    return this.http.get<Curso>(`${this.apiUrl}cursos_por_categoria/${idCategoria}/`);
  }

  // Realiza la adquisición de cursos para cliente logueado
  public adquirirCursos(token: string | null, cursos: Curso[]): Observable<any> {
    const data = { token, cursos };
    console.log(data)
    return this.http.post<any>(`${this.apiUrl}adquirir_curso/`, data);
  }
}
