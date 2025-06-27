import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:csv/csv.dart';

void main() {
  runApp(const PalBreedingApp());
}

class PalBreedingApp extends StatelessWidget {
  const PalBreedingApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '팰 조합 계산기',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const PalBreedingScreen(),
    );
  }
}

class BreedingResult {
  final String parent1Id;
  final String parent2Id;
  final String childId;
  
  BreedingResult({
    required this.parent1Id,
    required this.parent2Id,
    required this.childId,
  });
}

enum SearchMode {
  findChild,    // 부모1 + 부모2 → 자식 찾기
  findParent2,  // 부모1 + 자식 → 부모2 찾기
  findParent1,  // 부모2 + 자식 → 부모1 찾기
  smartSearch,  // 스마트 검색 (하나만 선택해도 관련 조합 표시)
}

class PalData {
  final String id;
  final String name;
  
  PalData({required this.id, required this.name});
}

class PalBreedingScreen extends StatefulWidget {
  const PalBreedingScreen({super.key});

  @override
  State<PalBreedingScreen> createState() => _PalBreedingScreenState();
}

class _PalBreedingScreenState extends State<PalBreedingScreen> {
  List<List<dynamic>> breedingData = [];
  List<PalData> allPals = [];
  Map<String, String> nameToIdMap = {}; // 이름 -> ID 매핑
  Map<String, String> idToNameMap = {}; // ID -> 이름 매핑
  
  String? selectedParent1Id;
  String? selectedParent2Id;
  String? selectedChildId;
  
  List<BreedingResult> smartSearchResults = [];
  bool isLoading = true;
  SearchMode searchMode = SearchMode.smartSearch;

  @override
  void initState() {
    super.initState();
    loadPalData();
  }

  Future<void> loadPalData() async {
    try {
      print('📊 데이터 로딩 시작...');
      
      // pal_list.csv 로드
      print('📂 pal_list.csv 로딩 중...');
      final palListData = await rootBundle.loadString('assets/data/pal_list.csv');
      // 수동으로 CSV 파싱
      final lines = palListData.trim().split('\n');
      
      List<List<String>> palListTable = [];
      for (String line in lines) {
        final trimmedLine = line.trim();
        if (trimmedLine.isNotEmpty) {
          final columns = trimmedLine.split(',');
          palListTable.add(columns.map((col) => col.trim()).toList());
        }
      }
      
      print('✅ pal_list.csv 로드 완료: ${palListTable.length}행');
      
      // ID-이름 매핑 생성
      Map<String, String> tempNameToIdMap = {};
      Map<String, String> tempIdToNameMap = {};
      List<PalData> tempAllPals = [];
      
      for (int i = 1; i < palListTable.length; i++) { // 헤더 제외
        if (palListTable[i].length >= 2) {
          String id = palListTable[i][0].toString();
          String name = palListTable[i][1].toString();
          
          tempNameToIdMap[name] = id;
          tempIdToNameMap[id] = name;
          tempAllPals.add(PalData(id: id, name: name));
        }
      }
      print('✅ 팰 데이터 매핑 완료: ${tempAllPals.length}개');
      
      // breeding data 로드
      print('📂 breeding_data.csv 로딩 중...');
      final csvData = await rootBundle.loadString('assets/data/paldb_breeding_data_ui_driven.csv');
      final List<List<dynamic>> csvTable = const CsvToListConverter().convert(csvData);
      print('✅ breeding_data.csv 로드 완료: ${csvTable.length}행');
      
      setState(() {
        nameToIdMap = tempNameToIdMap;
        idToNameMap = tempIdToNameMap;
        allPals = tempAllPals..sort((a, b) => a.name.compareTo(b.name));
        breedingData = csvTable;
        isLoading = false;
      });
      
      print('🎉 모든 데이터 로딩 완료!');
      print('- 팰 개수: ${allPals.length}');
      print('- 조합 데이터: ${breedingData.length}행');
      
    } catch (e) {
      print('❌ 데이터 로딩 오류: $e');
      setState(() {
        isLoading = false;
      });
    }
  }

  void performSmartSearch() {
    List<BreedingResult> results = [];
    
    // 선택된 팰들 확인
    bool hasParent1 = selectedParent1Id != null;
    bool hasParent2 = selectedParent2Id != null;
    bool hasChild = selectedChildId != null;
    
    for (int i = 1; i < breedingData.length; i++) {
      if (breedingData[i].length >= 3) {
        String breedingParent1Name = breedingData[i][1].toString();
        String breedingParent2Name = breedingData[i][2].toString();
        String breedingChildName = breedingData[i][0].toString();
        
        String? breedingParent1Id = nameToIdMap[breedingParent1Name];
        String? breedingParent2Id = nameToIdMap[breedingParent2Name];
        String? breedingChildId = nameToIdMap[breedingChildName];
        
        if (breedingParent1Id == null || breedingParent2Id == null || breedingChildId == null) {
          continue;
        }
        
        bool matches = false;
        
        if (hasParent1 && !hasParent2 && !hasChild) {
          // 부모1만 선택된 경우: 이 팰이 부모로 참여하는 모든 조합
          matches = (breedingParent1Id == selectedParent1Id || breedingParent2Id == selectedParent1Id);
        } else if (!hasParent1 && hasParent2 && !hasChild) {
          // 부모2만 선택된 경우: 이 팰이 부모로 참여하는 모든 조합
          matches = (breedingParent1Id == selectedParent2Id || breedingParent2Id == selectedParent2Id);
        } else if (!hasParent1 && !hasParent2 && hasChild) {
          // 자식만 선택된 경우: 이 팰을 만드는 모든 부모 조합
          matches = (breedingChildId == selectedChildId);
        } else if (hasParent1 && hasParent2 && !hasChild) {
          // 부모 둘 다 선택된 경우: 정확한 조합으로 만들 수 있는 자식
          matches = ((breedingParent1Id == selectedParent1Id && breedingParent2Id == selectedParent2Id) ||
                    (breedingParent1Id == selectedParent2Id && breedingParent2Id == selectedParent1Id));
        } else if (hasParent1 && !hasParent2 && hasChild) {
          // 부모1 + 자식 선택된 경우: 부모2 찾기
          matches = (breedingChildId == selectedChildId && 
                    (breedingParent1Id == selectedParent1Id || breedingParent2Id == selectedParent1Id));
        } else if (!hasParent1 && hasParent2 && hasChild) {
          // 부모2 + 자식 선택된 경우: 부모1 찾기
          matches = (breedingChildId == selectedChildId && 
                    (breedingParent1Id == selectedParent2Id || breedingParent2Id == selectedParent2Id));
        }
        
        if (matches) {
          // 중복 제거
          bool isDuplicate = results.any((result) =>
            result.parent1Id == breedingParent1Id &&
            result.parent2Id == breedingParent2Id &&
            result.childId == breedingChildId);
          
          if (!isDuplicate) {
            results.add(BreedingResult(
              parent1Id: breedingParent1Id,
              parent2Id: breedingParent2Id,
              childId: breedingChildId,
            ));
          }
        }
      }
    }
    
    setState(() {
      smartSearchResults = results;
    });
  }

  String getPalImagePath(String palId) {
    // ID 기반으로 이미지 경로 생성
    return 'assets/images/pals/${palId}_menu.webp';
  }

  String getFallbackPalImagePath(String palId) {
    // 기존 이름 기반 이미지 경로 생성 (fallback용)
    String palName = idToNameMap[palId] ?? 'Unknown';
    String fileName = palName.replaceAll(' ', '_');
    return 'assets/images/pals/${fileName}_menu.webp';
  }

  Widget buildPalImage(String palId, {double? width, double? height, double? iconSize}) {
    return Image.asset(
      getPalImagePath(palId),
      width: width,
      height: height,
      fit: BoxFit.contain,
      errorBuilder: (context, error, stackTrace) {
        // ID 기반 이미지가 없으면 이름 기반으로 fallback 시도
        return Image.asset(
          getFallbackPalImagePath(palId),
          width: width,
          height: height,
          fit: BoxFit.contain,
          errorBuilder: (context, error, stackTrace) {
            // 둘 다 없으면 기본 아이콘 표시
            return Icon(
              Icons.image_not_supported, 
              size: iconSize ?? 30,
            );
          },
        );
      },
    );
  }

  static Widget buildPalImageStatic(String palId, Map<String, String> idToNameMap, {double? width, double? height, double? iconSize}) {
    String getPalImagePath(String palId) {
      return 'assets/images/pals/${palId}_menu.webp';
    }
    
    String getFallbackPalImagePath(String palId) {
      String palName = idToNameMap[palId] ?? 'Unknown';
      String fileName = palName.replaceAll(' ', '_');
      return 'assets/images/pals/${fileName}_menu.webp';
    }
    
    return Image.asset(
      getPalImagePath(palId),
      width: width,
      height: height,
      fit: BoxFit.contain,
      errorBuilder: (context, error, stackTrace) {
        // ID 기반 이미지가 없으면 이름 기반으로 fallback 시도
        return Image.asset(
          getFallbackPalImagePath(palId),
          width: width,
          height: height,
          fit: BoxFit.contain,
          errorBuilder: (context, error, stackTrace) {
            // 둘 다 없으면 기본 아이콘 표시
            return Icon(
              Icons.image_not_supported, 
              size: iconSize ?? 30,
            );
          },
        );
      },
    );
  }

  String getPalName(String palId) {
    return idToNameMap[palId] ?? 'Unknown';
  }

  Future<void> showPalSelector({
    required String title,
    required String? currentSelectionId,
    required Function(String) onPalSelected,
  }) async {
    final selectedId = await showModalBottomSheet<String>(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => PalSelectorModal(
        title: title,
        pals: allPals,
        currentSelectionId: currentSelectionId,
        getPalImagePath: getPalImagePath,
        idToNameMap: idToNameMap,
      ),
    );
    
    if (selectedId != null) {
      onPalSelected(selectedId);
    }
  }

  Widget buildPalSelectorButton({
    required String label,
    required String? selectedPalId,
    required VoidCallback onTap,
    required bool isEnabled,
  }) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: TextStyle(
            fontSize: 16, 
            fontWeight: FontWeight.bold,
            color: isEnabled ? Colors.black : Colors.grey,
          ),
        ),
        const SizedBox(height: 8),
        InkWell(
          onTap: isEnabled ? onTap : null,
          child: Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              border: Border.all(color: isEnabled ? Colors.grey : Colors.grey.shade300),
              borderRadius: BorderRadius.circular(8),
              color: isEnabled ? Colors.white : Colors.grey.shade100,
            ),
            child: selectedPalId == null
                ? Row(
                    children: [
                      Icon(
                        Icons.add_circle_outline,
                        color: isEnabled ? Colors.grey : Colors.grey.shade400,
                      ),
                      const SizedBox(width: 12),
                      Text(
                        '팰을 선택하세요',
                        style: TextStyle(
                          fontSize: 16,
                          color: isEnabled ? Colors.grey : Colors.grey.shade400,
                        ),
                      ),
                    ],
                  )
                : Row(
                    children: [
                      Container(
                        width: 50,
                        height: 50,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: Colors.grey),
                        ),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(8),
                          child: buildPalImage(selectedPalId),
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Text(
                          getPalName(selectedPalId),
                          style: const TextStyle(fontSize: 16),
                        ),
                      ),
                      if (isEnabled)
                        IconButton(
                          icon: const Icon(Icons.clear),
                          onPressed: () {
                            setState(() {
                              if (label == '부모 팰 1') {
                                selectedParent1Id = null;
                              } else if (label == '부모 팰 2') {
                                selectedParent2Id = null;
                              } else if (label == '자식 팰') {
                                selectedChildId = null;
                              }
                              performSmartSearch();
                            });
                          },
                        ),
                    ],
                  ),
          ),
        ),
      ],
    );
  }

  String getSearchModeTitle() {
    switch (searchMode) {
      case SearchMode.findChild:
        return '자식 팰을 찾아보세요!';
      case SearchMode.findParent2:
        return '부모 팰 2를 찾아보세요!';
      case SearchMode.findParent1:
        return '부모 팰 1을 찾아보세요!';
      case SearchMode.smartSearch:
        return '스마트 조합 검색';
    }
  }

  String getSearchModeDescription() {
    switch (searchMode) {
      case SearchMode.findChild:
        return '부모 팰 1과 부모 팰 2를 선택하세요';
      case SearchMode.findParent2:
        return '부모 팰 1과 자식 팰을 선택하세요';
      case SearchMode.findParent1:
        return '부모 팰 2와 자식 팰을 선택하세요';
      case SearchMode.smartSearch:
        return '팰을 하나 이상 선택하면 관련된 모든 조합을 보여드립니다';
    }
  }

  void clearSelections() {
    setState(() {
      selectedParent1Id = null;
      selectedParent2Id = null;
      selectedChildId = null;
      smartSearchResults.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    if (isLoading) {
      return const Scaffold(
        body: Center(
          child: CircularProgressIndicator(),
        ),
      );
    }

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('팰 조합 계산기'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // 검색 모드 선택 라디오 버튼
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: Colors.grey.shade50,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: Colors.grey.shade300),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    '검색 모드 선택',
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 10),
                  RadioListTile<SearchMode>(
                    title: const Text('🔍 스마트 검색 (추천)'),
                    subtitle: const Text('팰 하나만 선택해도 관련 조합 자동 표시'),
                    value: SearchMode.smartSearch,
                    groupValue: searchMode,
                    onChanged: (SearchMode? value) {
                      setState(() {
                        searchMode = value!;
                        clearSelections();
                      });
                    },
                  ),
                  RadioListTile<SearchMode>(
                    title: const Text('자식 팰 찾기'),
                    subtitle: const Text('부모1 + 부모2 → 자식'),
                    value: SearchMode.findChild,
                    groupValue: searchMode,
                    onChanged: (SearchMode? value) {
                      setState(() {
                        searchMode = value!;
                        clearSelections();
                      });
                    },
                  ),
                  RadioListTile<SearchMode>(
                    title: const Text('부모 팰 2 찾기'),
                    subtitle: const Text('부모1 + 자식 → 부모2'),
                    value: SearchMode.findParent2,
                    groupValue: searchMode,
                    onChanged: (SearchMode? value) {
                      setState(() {
                        searchMode = value!;
                        clearSelections();
                      });
                    },
                  ),
                  RadioListTile<SearchMode>(
                    title: const Text('부모 팰 1 찾기'),
                    subtitle: const Text('부모2 + 자식 → 부모1'),
                    value: SearchMode.findParent1,
                    groupValue: searchMode,
                    onChanged: (SearchMode? value) {
                      setState(() {
                        searchMode = value!;
                        clearSelections();
                      });
                    },
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            
            Text(
              getSearchModeTitle(),
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
            ),
            Text(
              getSearchModeDescription(),
              style: const TextStyle(fontSize: 14, color: Colors.grey),
            ),
            const SizedBox(height: 15),
            
            Expanded(
              child: SingleChildScrollView(
                child: Column(
                  children: [
                    // 부모 팰 1 선택
                    buildPalSelectorButton(
                      label: '부모 팰 1',
                      selectedPalId: selectedParent1Id,
                      onTap: () => showPalSelector(
                        title: '부모 팰 1 선택',
                        currentSelectionId: selectedParent1Id,
                        onPalSelected: (palId) {
                          setState(() {
                            selectedParent1Id = palId;
                            performSmartSearch();
                          });
                        },
                      ),
                      isEnabled: true,
                    ),
                    const SizedBox(height: 20),
                    
                    // 부모 팰 2 선택
                    buildPalSelectorButton(
                      label: '부모 팰 2',
                      selectedPalId: selectedParent2Id,
                      onTap: () => showPalSelector(
                        title: '부모 팰 2 선택',
                        currentSelectionId: selectedParent2Id,
                        onPalSelected: (palId) {
                          setState(() {
                            selectedParent2Id = palId;
                            performSmartSearch();
                          });
                        },
                      ),
                      isEnabled: true,
                    ),
                    const SizedBox(height: 20),
                    
                    // 자식 팰 선택
                    buildPalSelectorButton(
                      label: '자식 팰',
                      selectedPalId: selectedChildId,
                      onTap: () => showPalSelector(
                        title: '자식 팰 선택',
                        currentSelectionId: selectedChildId,
                        onPalSelected: (palId) {
                          setState(() {
                            selectedChildId = palId;
                            performSmartSearch();
                          });
                        },
                      ),
                      isEnabled: true,
                    ),
                    const SizedBox(height: 20),
                    
                    // 결과 표시
                    if (smartSearchResults.isNotEmpty) ...[
                      Container(
                        padding: const EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          color: Colors.blue.shade50,
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: Colors.blue.shade200),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              '조합 결과: ${smartSearchResults.length}개',
                              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                            ),
                            const SizedBox(height: 10),
                            ListView.builder(
                              shrinkWrap: true,
                              physics: const NeverScrollableScrollPhysics(),
                              itemCount: smartSearchResults.length,
                              itemBuilder: (context, index) {
                                final result = smartSearchResults[index];
                                return Container(
                                  margin: const EdgeInsets.only(bottom: 8),
                                  padding: const EdgeInsets.all(12),
                                  decoration: BoxDecoration(
                                    color: Colors.white,
                                    borderRadius: BorderRadius.circular(8),
                                    border: Border.all(color: Colors.grey.shade300),
                                  ),
                                  child: Row(
                                    children: [
                                      // 부모 1
                                      Expanded(
                                        child: Column(
                                          children: [
                                            Container(
                                              width: 40,
                                              height: 40,
                                              decoration: BoxDecoration(
                                                borderRadius: BorderRadius.circular(6),
                                                border: Border.all(color: Colors.grey.shade300),
                                              ),
                                              child: ClipRRect(
                                                borderRadius: BorderRadius.circular(6),
                                                child: buildPalImage(result.parent1Id, iconSize: 20),
                                              ),
                                            ),
                                            const SizedBox(height: 4),
                                            Text(
                                              getPalName(result.parent1Id),
                                              style: const TextStyle(fontSize: 11),
                                              textAlign: TextAlign.center,
                                              maxLines: 2,
                                              overflow: TextOverflow.ellipsis,
                                            ),
                                          ],
                                        ),
                                      ),
                                      const Icon(Icons.add, color: Colors.grey),
                                      // 부모 2
                                      Expanded(
                                        child: Column(
                                          children: [
                                            Container(
                                              width: 40,
                                              height: 40,
                                              decoration: BoxDecoration(
                                                borderRadius: BorderRadius.circular(6),
                                                border: Border.all(color: Colors.grey.shade300),
                                              ),
                                              child: ClipRRect(
                                                borderRadius: BorderRadius.circular(6),
                                                child: buildPalImage(result.parent2Id, iconSize: 20),
                                              ),
                                            ),
                                            const SizedBox(height: 4),
                                            Text(
                                              getPalName(result.parent2Id),
                                              style: const TextStyle(fontSize: 11),
                                              textAlign: TextAlign.center,
                                              maxLines: 2,
                                              overflow: TextOverflow.ellipsis,
                                            ),
                                          ],
                                        ),
                                      ),
                                      const Icon(Icons.arrow_forward, color: Colors.blue),
                                      // 자식
                                      Expanded(
                                        child: Column(
                                          children: [
                                            Container(
                                              width: 40,
                                              height: 40,
                                              decoration: BoxDecoration(
                                                borderRadius: BorderRadius.circular(6),
                                                border: Border.all(color: Colors.blue.shade300),
                                                color: Colors.blue.shade50,
                                              ),
                                              child: ClipRRect(
                                                borderRadius: BorderRadius.circular(6),
                                                child: buildPalImage(result.childId, iconSize: 20),
                                              ),
                                            ),
                                            const SizedBox(height: 4),
                                            Text(
                                              getPalName(result.childId),
                                              style: const TextStyle(
                                                fontSize: 11,
                                                fontWeight: FontWeight.bold,
                                                color: Colors.blue,
                                              ),
                                              textAlign: TextAlign.center,
                                              maxLines: 2,
                                              overflow: TextOverflow.ellipsis,
                                            ),
                                          ],
                                        ),
                                      ),
                                    ],
                                  ),
                                );
                              },
                            ),
                          ],
                        ),
                      ),
                    ] else if (selectedParent1Id != null || selectedParent2Id != null || selectedChildId != null) ...[
                      Container(
                        padding: const EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          color: Colors.grey.shade100,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: const Row(
                          children: [
                            Icon(Icons.info_outline, color: Colors.grey),
                            SizedBox(width: 8),
                            Text(
                              '해당 조합 결과가 없습니다.',
                              style: TextStyle(fontSize: 16, color: Colors.grey),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class PalSelectorModal extends StatefulWidget {
  final String title;
  final List<PalData> pals;
  final String? currentSelectionId;
  final String Function(String) getPalImagePath;
  final Map<String, String> idToNameMap;

  const PalSelectorModal({
    super.key,
    required this.title,
    required this.pals,
    required this.currentSelectionId,
    required this.getPalImagePath,
    required this.idToNameMap,
  });

  @override
  State<PalSelectorModal> createState() => _PalSelectorModalState();
}

class _PalSelectorModalState extends State<PalSelectorModal> {
  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      height: MediaQuery.of(context).size.height * 0.85,
      decoration: const BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      child: Column(
        children: [
          // 헤더
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.grey.shade50,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(20)),
            ),
            child: Row(
              children: [
                Expanded(
                  child: Text(
                    widget.title,
                    style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.close),
                  onPressed: () => Navigator.pop(context),
                ),
              ],
            ),
          ),
          
          // 팰 목록
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.all(16),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                crossAxisSpacing: 10,
                mainAxisSpacing: 10,
                childAspectRatio: 1.2,
              ),
              itemCount: widget.pals.length,
              itemBuilder: (context, index) {
                final pal = widget.pals[index];
                final isSelected = pal.id == widget.currentSelectionId;
                
                return InkWell(
                  onTap: () => Navigator.pop(context, pal.id),
                  child: Container(
                    decoration: BoxDecoration(
                      border: Border.all(
                        color: isSelected ? Colors.blue : Colors.grey.shade300,
                        width: isSelected ? 2 : 1,
                      ),
                      borderRadius: BorderRadius.circular(12),
                      color: isSelected ? Colors.blue.shade50 : Colors.white,
                    ),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        if (isSelected)
                          const Padding(
                            padding: EdgeInsets.only(bottom: 4),
                            child: Icon(
                              Icons.check_circle,
                              color: Colors.blue,
                              size: 20,
                            ),
                          ),
                        Container(
                          width: 60,
                          height: 60,
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(8),
                            border: Border.all(color: Colors.grey.shade300),
                          ),
                          child: ClipRRect(
                            borderRadius: BorderRadius.circular(8),
                            child: _PalBreedingScreenState.buildPalImageStatic(
                              pal.id,
                              widget.idToNameMap,
                              width: 60,
                              height: 60,
                              iconSize: 30,
                            ),
                          ),
                        ),
                        const SizedBox(height: 8),
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 4),
                          child: Text(
                            pal.name,
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                              color: isSelected ? Colors.blue : Colors.black,
                            ),
                            textAlign: TextAlign.center,
                            maxLines: 2,
                            overflow: TextOverflow.ellipsis,
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }


}
