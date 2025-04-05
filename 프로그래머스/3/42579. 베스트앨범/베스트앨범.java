import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        
        Map<String, Integer> genrePlayCount = new HashMap<>(); // 장르별 재생횟수
        Map<String, List<Song>> genreToSongs = new HashMap<>(); // 장르별 노래 리스트
        
        for (int i=0; i<genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            
            // 1. 장르별 총 재생 수 누적
            genrePlayCount.put(genre, genrePlayCount.getOrDefault(genre, 0) + play);
            
            // 2. 장르별 노래 리스트
            genreToSongs.putIfAbsent(genre, new ArrayList<>());
            genreToSongs.get(genre).add(new Song(i, play));
        }
        // 3. 장르별 총 재생 수 기준 내림차순 정렬
        List<String> sortedGenres = new ArrayList<>(genrePlayCount.keySet());
        sortedGenres.sort((a, b) -> genrePlayCount.get(b) - genrePlayCount.get(a));
        
        List<Integer> result = new ArrayList<>();
        
        for (String genre: sortedGenres) {
            List<Song> songs = genreToSongs.get(genre);
            
            // 4. 해당 장르의 노래를 재생수 내림차순, 인덱스 오름차순 정렬
            songs.sort((s1, s2) -> {
                if (s1.play != s2.play) return s2.play - s1.play;
                else return s1.index - s2.index;
            });
            
            // 5. 장르별로 최대 2개 선택
            for (int i=0; i<Math.min(songs.size(), 2); i++) {
                result.add(songs.get(i).index);
            }  
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
    
    // 내부 클래스: 고유번호와 재생수를 가진 Song
    static class Song {
        int index;
        int play;

        Song(int index, int play) {
            this.index = index;
            this.play = play;
        }
    }
}